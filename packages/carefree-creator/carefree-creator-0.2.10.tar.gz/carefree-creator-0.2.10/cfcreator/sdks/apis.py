# `apis` sdk is used to prgrammatically call the algorithms.

import time

from cfcreator import *
from PIL import Image
from typing import Any
from typing import Dict
from typing import List
from typing import Union
from typing import Optional
from pydantic import BaseModel
from collections import OrderedDict
from cftool.misc import get_err_msg
from cftool.misc import random_hash
from cftool.misc import print_warning
from cftool.misc import shallow_copy_dict
from cftool.data_structures import Workflow
from cftool.data_structures import WorkNode
from cftool.data_structures import InjectionPack
from cfclient.core import HttpClient
from cfclient.utils import download_image_with_retry
from cfclient.models import TextModel
from cfclient.models import ImageModel
from cfclient.models import algorithms as registered_algorithms
from cflearn.api.cv.diffusion import ControlNetHints


TRes = Union[List[Union[str, int, float]], List[Image.Image]]
UPLOAD_ENDPOINT = "$upload"
ADD_TEXT_ENDPOINT = "$add_text"
CONTROL_HINT_ENDPOINT = "$control_hint"
FOR_EACH_ENDPOINT = "$for_each"
PICK_ENDPOINT = "$pick"
ALL_LATENCIES_KEY = "$all_latencies"
EXCEPTION_MESSAGE_KEY = "$exception_message"
endpoint2method = {
    txt2img_sd_endpoint: "txt2img",
    txt2img_sd_inpainting_endpoint: "sd_inpainting",
    txt2img_sd_outpainting_endpoint: "sd_outpainting",
    img2img_sd_endpoint: "img2img",
    img2img_sr_endpoint: "sr",
    img2img_sod_endpoint: "sod",
    img2img_inpainting_endpoint: "inpainting",
    img2img_semantic2img_endpoint: "semantic2img",
    img2img_harmonization_endpoint: "harmonization",
    img2txt_caption_endpoint: "image_captioning",
    txt2txt_prompt_enhance_endpoint: "prompt_enhance",
    new_control_multi_endpoint: "run_multi_controlnet",
    upscale_tile_endpoint: "upscale_tile",
    cv_blur_endpoint: "blur",
    cv_grayscale_endpoint: "grayscale",
    cv_erode_endpoint: "erode",
    cv_resize_endpoint: "resize",
    cv_affine_endpoint: "affine",
    cv_get_mask_endpoint: "get_mask",
    cv_inverse_endpoint: "inverse",
    cv_fill_bg_endpoint: "fill_bg",
    cv_get_size_endpoint: "get_size",
    cv_modify_box_endpoint: "modify_box",
    cv_generate_masks_endpoint: "generate_masks",
    cv_crop_image_endpoint: "crop_image",
    cv_histogram_match_endpoint: "histogram_match",
    cv_image_similarity_endpoint: "image_similarity",
    cv_repositioning_endpoint: "repositioning",
    facexlib_parse_endpoint: "facexlib_parse",
    facexlib_detect_endpoint: "facexlib_detect",
    paste_pipeline_endpoint: "paste_pipeline",
    UPLOAD_ENDPOINT: "get_image",
    ADD_TEXT_ENDPOINT: "add_text",
    CONTROL_HINT_ENDPOINT: "get_control_hint",
    FOR_EACH_ENDPOINT: "for_each",
    PICK_ENDPOINT: "pick",
}


class ForEachModel(BaseModel):
    endpoint: str
    loops: Dict[str, List[Any]]
    params: Dict[str, Any]
    loop_backs: Optional[List[InjectionPack]] = None


class PickModel(BaseModel):
    index: int
    values: List[Any]


class APIs:
    algorithms: Dict[str, IAlgorithm]

    def __init__(
        self,
        *,
        clients: Optional[dict] = None,
        algorithms: Optional[Dict[str, IAlgorithm]] = None,
        focuses_endpoints: Optional[List[str]] = None,
        excludes_endpoints: Optional[List[str]] = None,
        verbose: Optional[Union[str, bool]] = "auto",
        lazy_load: Optional[bool] = True,
    ) -> None:
        if focuses_endpoints is None:
            focuses = None
        else:
            focuses = list(map(endpoint2algorithm, focuses_endpoints))
        if excludes_endpoints is None:
            excludes = None
        else:
            excludes = list(map(endpoint2algorithm, excludes_endpoints))
        if verbose is not None:
            if verbose == "auto":
                verbose = focuses is not None
            OPT["verbose"] = verbose
        if lazy_load is not None:
            OPT["lazy_load"] = lazy_load

        self._is_new_http_client = False
        if clients is None:
            self._is_new_http_client = True
            self._http_client = HttpClient()
            clients = dict(http=self._http_client, triton=None)
        else:
            self._http_client = clients.get("http")
            if self._http_client is None:
                print_warning(f"cannot find `http` client in {clients}, creating one")
                self._is_new_http_client = True
                self._http_client = HttpClient()
                clients["http"] = self._http_client
        if algorithms is not None:
            self.algorithms = algorithms
        else:
            self.algorithms = {
                k: v(clients)
                for k, v in registered_algorithms.items()
                if (focuses is None or k in focuses)
                and (excludes is None or k not in excludes)
            }
            for v in self.algorithms.values():
                if isinstance(v, IWrapperAlgorithm):
                    v.algorithms = self.algorithms
                v.initialize()
        if self._is_new_http_client:
            self._http_client.start()

    # lifecycle

    async def destroy(self) -> None:
        if self._is_new_http_client:
            await self._http_client.stop()

    # algorithms

    async def _run(
        self, data: BaseModel, endpoint: str, **kw: Any
    ) -> List[Image.Image]:
        if isinstance(data, ReturnArraysModel):
            data.return_arrays = True
        task = endpoint2algorithm(endpoint)
        arrays = await self.algorithms[task].run(data, **kw)
        return list(map(Image.fromarray, arrays))

    async def txt2img(self, data: Txt2ImgSDModel, **kw: Any) -> List[Image.Image]:
        return await self._run(data, txt2img_sd_endpoint, **kw)

    async def img2img(self, data: Img2ImgSDModel, **kw: Any) -> List[Image.Image]:
        return await self._run(data, img2img_sd_endpoint, **kw)

    async def sr(self, data: Img2ImgSRModel, **kw: Any) -> List[Image.Image]:
        return await self._run(data, img2img_sr_endpoint, **kw)

    async def sod(self, data: Img2ImgSODModel, **kw: Any) -> List[Image.Image]:
        return await self._run(data, img2img_sod_endpoint, **kw)

    async def inpainting(
        self, data: Img2ImgInpaintingModel, **kw: Any
    ) -> List[Image.Image]:
        return await self._run(data, img2img_inpainting_endpoint, **kw)

    async def semantic2img(
        self, data: Img2ImgSemantic2ImgModel, **kw: Any
    ) -> List[Image.Image]:
        return await self._run(data, img2img_semantic2img_endpoint, **kw)

    async def sd_inpainting(
        self, data: Txt2ImgSDInpaintingModel, **kw: Any
    ) -> List[Image.Image]:
        return await self._run(data, txt2img_sd_inpainting_endpoint, **kw)

    async def sd_outpainting(
        self, data: Txt2ImgSDOutpaintingModel, **kw: Any
    ) -> List[Image.Image]:
        return await self._run(data, txt2img_sd_outpainting_endpoint, **kw)

    async def image_captioning(self, data: Img2TxtModel, **kw: Any) -> List[str]:
        task = endpoint2algorithm(img2txt_caption_endpoint)
        result: TextModel = await self.algorithms[task].run(data, **kw)
        return [result.text]

    async def run_multi_controlnet(
        self, data: ControlMultiModel, **kw: Any
    ) -> List[Image.Image]:
        return await self._run(data, new_control_multi_endpoint, **kw)

    async def harmonization(
        self, data: Img2ImgHarmonizationModel, **kw: Any
    ) -> List[Image.Image]:
        return await self._run(data, img2img_harmonization_endpoint, **kw)

    async def paste_pipeline(
        self, data: PastePipelineModel, **kw: Any
    ) -> List[Image.Image]:
        return await self._run(data, paste_pipeline_endpoint, **kw)

    async def blur(self, data: BlurModel, **kw: Any) -> List[Image.Image]:
        return await self._run(data, cv_blur_endpoint, **kw)

    async def grayscale(self, data: CVImageModel, **kw: Any) -> List[Image.Image]:
        return await self._run(data, cv_grayscale_endpoint, **kw)

    async def erode(self, data: ErodeModel, **kw: Any) -> List[Image.Image]:
        return await self._run(data, cv_erode_endpoint, **kw)

    async def resize(self, data: ResizeModel, **kw: Any) -> List[Image.Image]:
        return await self._run(data, cv_resize_endpoint, **kw)

    async def affine(self, data: AffineModel, **kw: Any) -> List[Image.Image]:
        return await self._run(data, cv_affine_endpoint, **kw)

    async def get_mask(self, data: CVImageModel, **kw: Any) -> List[Image.Image]:
        return await self._run(data, cv_get_mask_endpoint, **kw)

    async def inverse(self, data: CVImageModel, **kw: Any) -> List[Image.Image]:
        return await self._run(data, cv_inverse_endpoint, **kw)

    async def fill_bg(self, data: FillBGModel, **kw: Any) -> List[Image.Image]:
        return await self._run(data, cv_fill_bg_endpoint, **kw)

    async def get_size(self, data: ImageModel, **kw: Any) -> List[int]:
        task = endpoint2algorithm(cv_get_size_endpoint)
        return await self.algorithms[task].run(data, **kw)

    async def modify_box(self, data: ModifyBoxModel, **kw: Any) -> List[List[int]]:
        task = endpoint2algorithm(cv_modify_box_endpoint)
        return await self.algorithms[task].run(data, **kw)

    async def generate_masks(
        self, data: GenerateMasksModel, **kw: Any
    ) -> List[Image.Image]:
        return await self._run(data, cv_generate_masks_endpoint, **kw)

    async def crop_image(self, data: CropImageModel, **kw: Any) -> List[Image.Image]:
        return await self._run(data, cv_crop_image_endpoint, **kw)

    async def histogram_match(
        self, data: HistogramMatchModel, **kw: Any
    ) -> List[Image.Image]:
        return await self._run(data, cv_histogram_match_endpoint, **kw)

    async def image_similarity(
        self, data: ImageSimilarityModel, **kw: Any
    ) -> List[float]:
        task = endpoint2algorithm(cv_image_similarity_endpoint)
        result: ImageSimilarityResponse = await self.algorithms[task].run(data, **kw)
        return [result.similarity]

    async def repositioning(
        self, data: RepositioningModel, **kw: Any
    ) -> List[Image.Image]:
        return await self._run(data, cv_repositioning_endpoint, **kw)

    async def prompt_enhance(self, data: PromptEnhanceModel, **kw: Any) -> List[str]:
        task = endpoint2algorithm(txt2txt_prompt_enhance_endpoint)
        result: PromptEnhanceResponse = await self.algorithms[task].run(data)
        return result.prompts

    async def upscale_tile(
        self, data: UpscaleTileModel, **kw: Any
    ) -> List[Image.Image]:
        return await self._run(data, upscale_tile_endpoint, **kw)

    # third party

    async def facexlib_parse(
        self, data: FacexlibParseModel, **kw: Any
    ) -> List[Image.Image]:
        return await self._run(data, facexlib_parse_endpoint, **kw)

    async def facexlib_detect(
        self, data: FacexlibDetectModel, **kw: Any
    ) -> List[List[int]]:
        task = endpoint2algorithm(facexlib_detect_endpoint)
        result: FacexlibDetectResponse = await self.algorithms[task].run(data, **kw)
        return result.ltrbs

    # special

    async def get_image(self, data: ImageModel, **kw: Any) -> List[Image.Image]:
        image = await download_image_with_retry(self._http_client.session, data.url)
        return [image]

    async def add_text(self, data: TextModel, **kw: Any) -> List[str]:
        return [data.text]

    async def get_control_hint(
        self, hint_type: ControlNetHints, data: Dict[str, Any], **kw: Any
    ) -> List[Image.Image]:
        data = control_hint2hint_data_models[hint_type](**data)
        endpoint = control_hint2hint_endpoints[hint_type]
        return await self._run(data, endpoint, **kw)

    async def for_each(self, data: ForEachModel, **kw: Any) -> List[Any]:
        targets = []
        target_key = "$target"
        loop_back_key = "$loop_back"
        params_prefix = "params."
        get_cache_key = lambda k: f"$cache_{k}"
        keys = sorted(data.loops)
        value_lists = [data.loops[k] for k in keys]
        lengths = [len(l) for l in value_lists]
        if len(set(lengths)) != 1:
            msg = f"lengths of value_lists should be equal, got {lengths} (keys={keys})"
            raise ValueError(msg)
        base_caches = {}
        for i, i_values in enumerate(zip(*value_lists)):
            i_kw = shallow_copy_dict(kw)
            for k in list(i_kw):
                if k.startswith(params_prefix):
                    nk = k.lstrip(params_prefix)
                    i_kw[nk] = i_kw.pop(k)
            i_caches = {get_cache_key(k): [v] for k, v in zip(keys, i_values)}
            i_caches.update(shallow_copy_dict(base_caches))
            i_injections = {get_cache_key(k): {"index": 0, "field": k} for k in keys}
            if data.loop_backs is not None and i > 0:
                i_injections[loop_back_key] = data.loop_backs
            i_workflow = Workflow()
            i_workflow.push(
                WorkNode(
                    key=target_key,
                    endpoint=data.endpoint,
                    injections=i_injections,
                    data=shallow_copy_dict(data.params),
                )
            )
            i_results = await self.execute(i_workflow, target_key, i_caches, **i_kw)
            i_target = i_results[target_key]
            targets.append(i_target)
            if data.loop_backs is not None:
                base_caches[loop_back_key] = i_target
        return list(map(list, zip(*targets)))

    async def pick(self, data: PickModel, **kw: Any) -> List[Any]:
        return [data.values[data.index]]

    # workflow

    async def execute(
        self,
        workflow: Workflow,
        target: str,
        caches: Optional[Union[OrderedDict, Dict[str, Any]]] = None,
        *,
        return_if_exception: bool = False,
        **kwargs: Any,
    ) -> Dict[str, TRes]:
        def _inject(
            k: str,
            ki_cache: TRes,
            current_node_data: dict,
            is_for_each: bool = False,
        ) -> None:
            def _set_inject_with_loops_condition() -> None:
                if is_loops:
                    v0[next_k_with_loops_condition] = ki_cache
                else:
                    _inject(next_k_with_loops_condition, ki_cache, v0)

            k_split = k.split(".")
            k0 = k_split[0]
            v0 = current_node_data.get(k0)
            next_k_with_loops_condition = ".".join(k_split[1:])
            is_loops = is_for_each and k0 == "loops"
            if isinstance(v0, dict):
                _set_inject_with_loops_condition()
            elif isinstance(v0, (str, int, float)) or v0 is None:
                if len(k_split) == 1:
                    if isinstance(ki_cache, Image.Image):
                        # we assign random_hash here to make mapping possible
                        current_node_data[k0] = random_hash()
                    else:
                        current_node_data[k0] = ki_cache
                else:
                    if v0 is None:
                        v0 = current_node_data[k0] = {}
                        _set_inject_with_loops_condition()
                    else:
                        raise ValueError(
                            f"field under '{k0}' is already a vanilla value, "
                            f"but further keys are given: '{k_split[1:]}'"
                        )
            elif isinstance(v0, list):
                try:
                    k1 = int(k_split[1])
                except Exception:
                    raise ValueError(f"expected int key for '{k0}', got '{k_split[1]}'")
                v1 = v0[k1]
                if isinstance(v1, dict):
                    _inject(".".join(k_split[2:]), ki_cache, v1)
                elif len(k_split) == 2:
                    if isinstance(ki_cache, Image.Image):
                        # we assign random_hash here to make mapping possible
                        v0[k1] = random_hash()
                    else:
                        v0[k1] = ki_cache
                else:
                    raise ValueError(
                        f"list under '{k0}' is already a vanilla list, "
                        f"but further keys are given: '{k_split[2:]}'"
                    )
            else:
                raise ValueError(
                    f"field under '{k0}' should be one of "
                    "(BaseModel, str, int, float, list), "
                    f"but got '{type(v0)}'"
                )

        all_latencies = {}
        if caches is None:
            caches = OrderedDict()
        else:
            caches = OrderedDict(caches)
            workflow = workflow.copy().inject_caches(caches)
        try:
            for layer in workflow.get_dependency_path(target).hierarchy:
                for item in layer:
                    if item.key in caches:
                        continue
                    node = item.data
                    node_kw = shallow_copy_dict(kwargs)
                    node_data = shallow_copy_dict(node.data)
                    endpoint = node.endpoint
                    is_for_each = endpoint == FOR_EACH_ENDPOINT
                    for k, k_packs in node.injections.items():
                        if not isinstance(k_packs, list):
                            k_packs = [k_packs]
                        for k_pack in k_packs:
                            if k_pack.index is None:
                                ki_cache = caches[k]
                            else:
                                ki_cache = caches[k][k_pack.index]
                            _inject(k_pack.field, ki_cache, node_data, is_for_each)
                            if isinstance(ki_cache, Image.Image):
                                node_kw[k_pack.field] = ki_cache
                    method_fn = getattr(self, endpoint2method[endpoint])
                    t = time.time()
                    if endpoint == UPLOAD_ENDPOINT:
                        data_model = ImageModel(**node_data)
                        item_res = await method_fn(data_model, **node_kw)
                    elif endpoint == ADD_TEXT_ENDPOINT:
                        data_model = TextModel(**node_data)
                        item_res = await method_fn(data_model, **node_kw)
                    elif endpoint == CONTROL_HINT_ENDPOINT:
                        hint_type = node_data.pop("hint_type")
                        item_res = await method_fn(hint_type, node_data, **node_kw)
                        endpoint = control_hint2hint_endpoints[hint_type]
                    elif endpoint == FOR_EACH_ENDPOINT:
                        data_model = ForEachModel(**node_data)
                        item_res = await method_fn(data_model, **node_kw)
                    elif endpoint == PICK_ENDPOINT:
                        data_model = PickModel(**node_data)
                        item_res = await method_fn(data_model, **node_kw)
                    else:
                        data_model = self.get_data_model(endpoint, node_data)
                        item_res = await method_fn(data_model, **node_kw)
                    if endpoint == UPLOAD_ENDPOINT or endpoint == ADD_TEXT_ENDPOINT:
                        ls = dict(download=time.time() - t)
                    elif endpoint == FOR_EACH_ENDPOINT:
                        ls = dict(loop=time.time() - t)
                    elif endpoint == PICK_ENDPOINT:
                        ls = dict(pick=time.time() - t)
                    else:
                        ls = self.algorithms[
                            endpoint2algorithm(endpoint)
                        ].last_latencies
                    caches[item.key] = item_res
                    all_latencies[item.key] = ls
            caches[EXCEPTION_MESSAGE_KEY] = None
        except Exception as err:
            caches[EXCEPTION_MESSAGE_KEY] = get_err_msg(err)
            if not return_if_exception:
                raise err
        caches[ALL_LATENCIES_KEY] = all_latencies
        return caches

    # misc

    def get_data_model(self, endpoint: str, data: Dict[str, Any]) -> BaseModel:
        task = endpoint2algorithm(endpoint)
        return self.algorithms[task].model_class(**data)


__all__ = [
    "UPLOAD_ENDPOINT",
    "ADD_TEXT_ENDPOINT",
    "CONTROL_HINT_ENDPOINT",
    "FOR_EACH_ENDPOINT",
    "PICK_ENDPOINT",
    "ALL_LATENCIES_KEY",
    "APIs",
    "HighresModel",
    "Img2TxtModel",
    "Txt2ImgSDModel",
    "Img2ImgSDModel",
    "Img2ImgSRModel",
    "Img2ImgSODModel",
    "Img2ImgInpaintingModel",
    "Txt2ImgSDInpaintingModel",
    "Txt2ImgSDOutpaintingModel",
    "ControlNetHints",
    "ControlMultiModel",
    "Img2ImgHarmonizationModel",
]
