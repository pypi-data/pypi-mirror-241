from time import time
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytorch-pyramid",
    version="0.1.2",
    author="Henry Gong",
    author_email="henrygongzy@gmail.com",
    description="A gauss and laplacian pyramid implementation in pytorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Henry-GongZY/Image-Pyramid-pytorch",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)