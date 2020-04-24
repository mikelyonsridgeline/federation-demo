# TODO DEV: Replace all instances of <Service Name> with the name of your service
"""Provides the packaging instructions to deploy <Service Name> to a wheel/tar ball.

All commands below are to be run from the same directory that setup.py is in.

To package and install the <Service Name> package locally, run:
    pipenv install .

To package and install the <Service Name> package locally with the editable flag, run:
    pipenv install -e .

Note: in editable mode, local changes made to WIP libraries will be reflected
without needed to run the install command repeatedly.

To build the .whl/.tar.gz files for artifactory deployment, run:
    pipenv run python setup.py sdist bdist_wheel
"""
from setuptools import find_packages
from setuptools import setup

# TODO DEV: Fill in the values below with appropriate values for your service
setup(
    name="Service Template",
    version="0.1",
    description="A template for services based off of Pinecone",
    author="Sample Name",
    author_email="sample.name@ridgelineapps.com",
    # Product devs: do not change things below this line!
    package_dir={"": "src"},  #
    packages=find_packages("src"),
    zip_safe=False,
    install_requires=["pinecone"],
)
