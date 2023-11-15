import os
import cv2
import time
import torch

import numpy as np

from PIL import Image
from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import Tuple
from typing import Union
from typing import Optional
from fastapi import Response
from pydantic import Field
from pydantic import BaseModel
from cftool.cv import to_rgb
from cftool.cv import to_uint8
from cftool.cv import np_to_bytes
from cftool.cv import restrict_wh
from cftool.cv import get_suitable_size
from cfclient.models.core import ImageModel
from cflearn.api.cv.diffusion import ControlNetHints
from cflearn.models.cv.diffusion.utils import CONTROL_HINT_KEY
from cflearn.models.cv.diffusion.utils import CONTROL_HINT_END_KEY
from cflearn.models.cv.diffusion.utils import CONTROL_HINT_START_KEY

from .common import ControlNetModel
from ..utils import api_pool
from ..utils import to_canvas
from ..utils import resize_image
from ..utils import APIs
from ..common import BaseSDTag
from ..common import get_sd_from
from ..common import register_sd
from ..common import handle_diffusion_model
from ..common import handle_diffusion_inpainting_model
from ..common import IAlgorithm
from ..common import ReturnArraysModel


root = os.path.dirname(__file__)
control_depth_endpoint = "/control/depth"
control_canny_endpoint = "/control/canny"
control_pose_endpoint = "/control/pose"
control_mlsd_endpoint = "/control/mlsd"


images_type = Tuple[np.ndarray, np.ndarray]
apply_response = Tuple[List[np.ndarray], Dict[str, float]]


class ControlStrengthModel(BaseModel):
    control_strength: float = Field(1.0, description="The strength of the control.")


class ControlNetModelPlaceholder(ControlStrengthModel, ControlNetModel):
    pass


async def get_images(
    self: IAlgorithm,
    data: ControlNetModel,
    kwargs: Dict[str, Any],
) -> images_type:
    image = np.array(to_rgb(await self.get_image_from("url", data, kwargs)))
    if not data.hint_url:
        return image, image
    hint_image = np.array(to_rgb(await self.get_image_from("hint_url", data, kwargs)))
    return image, hint_image


def apply_control(
    data: Union[ControlNetModelPlaceholder, Dict[str, ControlNetModelPlaceholder]],
    api_key: APIs,
    input_image: np.ndarray,
    hint_image: np.ndarray,
    hint_types: Union[ControlNetHints, List[ControlNetHints]],
    normalized_inpainting_mask: Optional[np.ndarray] = None,
) -> apply_response:
    if not isinstance(data, dict):
        common_data = data
        detect_resolution = getattr(data, "detect_resolution", None)
    else:
        common_data = list(data.values())[0]
        detect_resolution = {}
        for hint_type, h_data in data.items():
            detect_resolution[hint_type] = getattr(h_data, "detect_resolution", None)
    t_sd = time.time()
    api = get_sd_from(api_key, common_data, no_change=True)
    need_change_device = api_pool.need_change_device(api_key)
    api.enable_control()
    original_h, original_w = input_image.shape[:2]
    resize_to_original = lambda array: cv2.resize(
        array,
        (original_w, original_h),
        interpolation=cv2.INTER_CUBIC,
    )
    w, h = restrict_wh(original_w, original_h, common_data.max_wh)
    w = get_suitable_size(w, 64)
    h = get_suitable_size(h, 64)
    t0 = time.time()
    if not isinstance(hint_types, list):
        hint_types = [hint_types]
    base_md = api.sd_weights.get(BaseSDTag) if common_data.no_switch else None
    api.switch_control(*hint_types, base_md=base_md)
    t1 = time.time()
    all_hint = {}
    all_o_hint_arrays = []
    all_annotator_change_device_times = []
    for hint_type in sorted(hint_types):
        if detect_resolution is None or isinstance(detect_resolution, int):
            h_res = detect_resolution
        else:
            h_res = detect_resolution.get(hint_type)
        if not isinstance(data, dict):
            h_data = data
        else:
            h_data = data.get(hint_type)
            if h_data is None:
                raise ValueError(f"cannot find data for '{hint_type}'")
        bypass_annotator = h_data.bypass_annotator
        if h_res is not None and not bypass_annotator:
            hint_image = resize_image(hint_image, h_res)
        device = api.device
        use_half = api.use_half
        ht = time.time()
        if need_change_device:
            device = "cuda:0"
            use_half = True
            api.annotators[hint_type].to(device, use_half=True)
        all_annotator_change_device_times.append(time.time() - ht)
        if bypass_annotator:
            o_hint_arr = np.array(hint_image)
        else:
            o_hint_arr = api.get_hint_of(hint_type, hint_image, **h_data.dict())
        ht = time.time()
        if need_change_device:
            api.annotators[hint_type].to("cpu", use_half=False)
            torch.cuda.empty_cache()
        all_annotator_change_device_times.append(time.time() - ht)
        hint_array = cv2.resize(o_hint_arr, (w, h), interpolation=cv2.INTER_LINEAR)
        hint = torch.from_numpy(hint_array)[None].permute(0, 3, 1, 2)
        if use_half:
            hint = hint.half()
        hint = hint.contiguous().to(device) / 255.0
        all_o_hint_arrays.append(o_hint_arr)
        all_hint[hint_type] = hint
    change_annotator_device_time = sum(all_annotator_change_device_times)
    t2 = time.time()
    num_scales = api.m.num_control_scales
    all_scales = {}
    for hint_type in sorted(hint_types):
        h_data = data[hint_type] if isinstance(data, dict) else data
        all_scales[hint_type] = (
            [
                h_data.control_strength * (0.825 ** float(12 - i))
                for i in range(num_scales)
            ]
            if h_data.guess_mode
            else ([h_data.control_strength] * num_scales)
        )
    cond = [common_data.prompt] * common_data.num_samples
    kw = handle_diffusion_model(api, common_data)
    keys = sorted([k.value if isinstance(k, ControlNetHints) else k for k in all_hint])
    kw[CONTROL_HINT_KEY] = [(k, all_hint[k]) for k in keys]
    kw[CONTROL_HINT_START_KEY] = [common_data.hint_starts.get(k) for k in keys]
    kw[CONTROL_HINT_END_KEY] = [common_data.hint_ends.get(k) for k in keys]
    kw["max_wh"] = common_data.max_wh
    api.m.control_scales = [all_scales[k] for k in keys]
    dt = time.time()
    if need_change_device:
        api.to("cuda:0", use_half=True, no_annotator=True)
    change_diffusion_device_time = time.time() - dt
    # inpainting workaround
    if api.m.unet_kw["in_channels"] == 9:
        if normalized_inpainting_mask is None:
            raise ValueError("`normalized_input_mask` should be provided to inpainting")
        image = Image.fromarray(input_image)
        inpainting_mask = Image.fromarray(to_uint8(normalized_inpainting_mask))
        kw.update(handle_diffusion_inpainting_model(common_data))
        outs = api.txt2img_inpainting(cond, image, inpainting_mask, **kw)
    elif not common_data.use_img2img:
        kw["size"] = w, h
        outs = api.txt2img(cond, **kw)
    else:
        init_image = cv2.resize(
            input_image,
            (w, h),
            interpolation=cv2.INTER_LINEAR,
        )
        init_image = init_image[None].repeat(common_data.num_samples, axis=0)
        init_image = init_image.transpose([0, 3, 1, 2])
        init_image = init_image.astype(np.float32) / 255.0
        kw["cond"] = cond
        kw["fidelity"] = common_data.fidelity
        init_tensor = torch.from_numpy(init_image)
        if api.use_half:
            init_tensor = init_tensor.half()
        init_tensor = init_tensor.to(api.device)
        outs = api.img2img(init_tensor, **kw)
    dt = time.time()
    change_diffusion_device_time += time.time() - dt
    outs = 0.5 * (outs + 1.0)
    outs = to_uint8(outs).permute(0, 2, 3, 1).cpu().numpy()
    t3 = time.time()
    results = list(map(resize_to_original, all_o_hint_arrays))
    for i in range(common_data.num_samples):
        results.append(resize_to_original(outs[i]))
    latencies = dict(
        get_model=t0 - t_sd,
        switch_control=t1 - t0,
        get_hint=t2 - t1 - change_annotator_device_time,
        change_annotator_device=change_annotator_device_time,
        inference=t3 - t2 - change_diffusion_device_time,
        change_diffusion_device=change_diffusion_device_time,
        post_resize=time.time() - t3,
    )
    return results, latencies


async def run_control(
    self: IAlgorithm,
    data: ControlNetModel,
    hint_type: ControlNetHints,
    kwargs: Dict[str, Any],
) -> Tuple[List[np.ndarray], Dict[str, float]]:
    self.log_endpoint(data)
    t0 = time.time()
    image, hint_image = await get_images(self, data, kwargs)
    t1 = time.time()
    results, latencies = apply_control(data, APIs.SD, image, hint_image, hint_type)
    latencies["download"] = t1 - t0
    return results, latencies


def register_control(
    algorithm_model_class: Type[ControlNetModel],
    algorithm_endpoint: str,
    hint_type: ControlNetHints,
) -> None:
    class _(IAlgorithm):
        model_class = algorithm_model_class

        endpoint = algorithm_endpoint

        def initialize(self) -> None:
            register_sd()

        async def run(
            self,
            data: algorithm_model_class,
            *args: Any,
            **kwargs: Any,
        ) -> Response:
            results, latencies = await run_control(self, data, hint_type, kwargs)
            t0 = time.time()
            content = None if data.return_arrays else np_to_bytes(to_canvas(results))
            t1 = time.time()
            latencies["to_canvas"] = t1 - t0
            self.log_times(latencies)
            if data.return_arrays:
                return results
            return Response(content=content, media_type="image/png")

    IAlgorithm.auto_register()(_)


def register_hint(
    hint_model_class: Type,
    hint_endpoint: str,
    hint_type: ControlNetHints,
) -> None:
    class _Model(hint_model_class, ReturnArraysModel, ImageModel):
        pass

    class _(IAlgorithm):
        model_class = _Model
        model_class.__name__ = hint_model_class.__name__

        endpoint = hint_endpoint

        def initialize(self) -> None:
            register_sd()

        async def run(self, data: _Model, *args: Any, **kwargs: Any) -> Response:
            t0 = time.time()
            image = await self.get_image_from("url", data, kwargs)
            w, h = image.size
            t1 = time.time()
            m = api_pool.get(APIs.SD)
            t2 = time.time()
            hint_image = np.array(image)
            detect_resolution = getattr(data, "detect_resolution", None)
            if detect_resolution is not None:
                hint_image = resize_image(hint_image, detect_resolution)
            hint = m.get_hint_of(hint_type, hint_image, **data.dict())
            hint = cv2.resize(hint, (w, h), interpolation=cv2.INTER_LINEAR)
            self.log_times(
                dict(
                    download=t1 - t0,
                    get_model=t2 - t1,
                    inference=time.time() - t2,
                )
            )
            if data.return_arrays:
                return [hint]
            return Response(content=np_to_bytes(hint), media_type="image/png")

    IAlgorithm.auto_register()(_)


class DetectResolutionModel(BaseModel):
    detect_resolution: int = Field(
        384,
        ge=128,
        le=1024,
        description="Detect resolution.",
    )


class LargeDetectResolutionModel(BaseModel):
    detect_resolution: int = Field(
        512,
        ge=128,
        le=1024,
        description="Detect resolution.",
    )


# ControlNet (depth2image)


class _DepthModel(DetectResolutionModel):
    pass


class DepthModel(_DepthModel, ControlStrengthModel):
    pass


class ControlDepthModel(DepthModel, ControlNetModel):
    pass


# ControlNet (canny2image)


class _CannyModel(LargeDetectResolutionModel):
    low_threshold: int = Field(
        100,
        ge=1,
        le=255,
        description="Low threshold of canny algorithm.",
    )
    high_threshold: int = Field(
        200,
        ge=1,
        le=255,
        description="High threshold of canny algorithm.",
    )


class CannyModel(_CannyModel, ControlStrengthModel):
    pass


class ControlCannyModel(CannyModel, ControlNetModel):
    pass


# ControlNet (pose2image)


class _PoseModel(LargeDetectResolutionModel):
    pass


class PoseModel(_PoseModel, ControlStrengthModel):
    pass


class ControlPoseModel(PoseModel, ControlNetModel):
    pass


# ControlNet (canny2image)


class _MLSDModel(LargeDetectResolutionModel):
    value_threshold: float = Field(
        0.1,
        ge=0.01,
        le=2.0,
        description="Value threshold of mlsd model.",
    )
    distance_threshold: float = Field(
        0.1,
        ge=0.01,
        le=20.0,
        description="Distance threshold of mlsd model.",
    )


class MLSDModel(_MLSDModel, ControlStrengthModel):
    pass


class ControlMLSDModel(MLSDModel, ControlNetModel):
    pass


# register

register_control(ControlDepthModel, control_depth_endpoint, ControlNetHints.DEPTH)
register_control(ControlCannyModel, control_canny_endpoint, ControlNetHints.CANNY)
register_control(ControlPoseModel, control_pose_endpoint, ControlNetHints.POSE)
register_control(ControlMLSDModel, control_mlsd_endpoint, ControlNetHints.MLSD)


__all__ = [
    "control_depth_endpoint",
    "control_canny_endpoint",
    "control_pose_endpoint",
    "control_mlsd_endpoint",
]
