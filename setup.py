from setuptools import setup, find_packages

setup(
    name="comon",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
