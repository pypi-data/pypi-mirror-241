from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()



print(long_description)

setup(
    name='exper',
    version='0.1.1',
    author="Mrzz",

    description="This is a python package for running deep learning experiments. "
                "Users can rapidly run their experiments by importing this module.",
    packages=find_packages(),
    install_requires=["torch", "torch_geometric"],
    include_package_data=True
)
