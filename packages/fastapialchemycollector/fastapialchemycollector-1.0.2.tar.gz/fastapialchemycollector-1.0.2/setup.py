from pathlib import Path

from pip._internal.req import parse_requirements
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
with open(this_directory / "README-public.md", encoding="utf8") as file_handle:
    long_description = file_handle.read()

VERSION = "1.0.2"

# pylint: disable=no-value-for-parameter
setup(
    name="fastapialchemycollector",
    version=VERSION,
    author="Metis dev",
    author_email="devops@metisdata.io",
    description="Metis log collector for FastAPI and SQLAlchemy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/metis-data/metis-python-collectors",
    project_urls={
        "Bug Tracker": "https://github.com/metis-data/metis-python-collectors/issues",
    },
    license="",
    packages=find_packages(),
    install_requires=[
        str(req.requirement)
        for req in parse_requirements("requirements.txt", session=False)
    ],
)
