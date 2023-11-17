import setuptools


with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "phenofit",
    version = "0.0.1",
    author = "Shen Pengju",
    author_email = "spjace@sina.com",
    description = "A small package for phenology analysis",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/spjace/phenofit",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)