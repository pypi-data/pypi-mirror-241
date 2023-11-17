import os.path
from setuptools import setup, find_packages

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name='managed-file-system-operator',
    version='0.0.1',
    author="Hyunsu An",
    author_email="ahs2202@gm.gist.ac.kr",
    description="A Python manager class implementing a variety of file system operations in a spawned process, supporting AWS (and AWS-like systems), HTTP, and the local file system.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ahs2202/managed-file-system-operator",
    license="GPLv3",
    packages=find_packages( ),
    include_package_data=True,
    install_requires=[
        "aiofiles>=23.2.1",
        "aiohttp>=3.8.5",
        "aioshutil>=1.3",
        "nest_asyncio>=1.5.6",
        "zarr>=2.16.0",
        "fsspec>=2023.6.0",
        "s3fs>=2023.6.0",
        "gcsfs>=2023.6.0",
    ],
)
