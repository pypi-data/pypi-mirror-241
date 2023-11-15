from setuptools import setup, find_packages

VERSION = "0.2.10"
PACKAGE_NAME = "carefree-creator"

DESCRIPTION = "An AI-powered creator for everyone."
with open("README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

kafka_requires = [
    "kafka-python",
    "redis[hiredis]",
    "cos-python-sdk-v5",
]
third_party_requires = [
    "facexlib",
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    entry_points={"console_scripts": ["cfcreator = cfcreator.cli:main"]},
    install_requires=[
        "click>=8.1.3",
        "fastapi==0.95.1",
        "pydantic<2.0.0",
        "carefree-toolkit>=0.3.9",
        "carefree-client>=0.1.10",
        "carefree-learn[cv_full]>=0.4.8",
        "networkx",
        "matplotlib",
    ],
    extras_require={
        "kafka": kafka_requires,
        "third_party": third_party_requires,
        "full": kafka_requires + third_party_requires,
    },
    author="carefree0910",
    author_email="syameimaru.saki@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords="python carefree-learn PyTorch",
)
