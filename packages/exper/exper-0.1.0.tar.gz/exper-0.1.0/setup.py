from distutils.core import setup
from setuptools import find_packages

setup(
    name='exper',
    version='0.1.0',
    author="Mrzz",
    description="This is a python exper for running deep learning experiments. "
                "Users can rapidly run their experiments by importing this exper.",
    packages=find_packages(),
    install_requires=["torch", "torch_geometric"],
    include_package_data=True
)
