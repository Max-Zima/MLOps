from setuptools import setup, find_packages
from glob import glob

so_files = glob("hadamard/python/*.so")

setup(
    name="hadamard",
    version="0.1",
    description="Python bindings for Hadamard product",
    packages=find_packages(),
    package_data={
        "hadamard": ["python/*.so"],
    },
)
