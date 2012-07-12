"""Setup the module
"""
from setuptools import setup, find_packages

setup(name="module_test",
      namespace_packages=["module"],
      packages=find_packages(),
      scripts=["scripts/importing_code.py"]
)
