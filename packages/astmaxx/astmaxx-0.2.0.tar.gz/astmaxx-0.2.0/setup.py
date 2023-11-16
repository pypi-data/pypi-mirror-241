import pathlib

import setuptools

setuptools.setup(
    name="astmaxx",
    version="0.2.0",
    description="astma codes",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/HV4512/astma_codes",
    author="Harsh Vardhan",
    author_email="jobbykarn@gmail.com",
    license="Open-Source",
    packages=setuptools.find_packages(),
    include_package_data=True,
    
)