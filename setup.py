# Install python package

from setuptools import find_packages, setup

# Return lines from filename
def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="netgraph",
    version="0.1.0",
    description="Discovery connections between servers in your network",
    # find_packages - Include all modules python at once (folders with __init__.py file inside)
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")},
)