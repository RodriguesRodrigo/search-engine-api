import sys
from setuptools import find_packages, setup

__required_python_version__ = (3, 7)
__version__ = "0.0.1"
__description__ = "Search Engine API"
__long_description__ = "Project that performs the search by name"

__author__ = "Rodrigo Rodrigues Scotti"
__author_email__ = "rrscotti@hotmail.com"

CURRENT_PYTHON_VERSION = sys.version_info[:2]

if CURRENT_PYTHON_VERSION < __required_python_version__:
    sys.stderr.write(
        "Unsupported Python {}.{}. Please change to {}.{} or higher.".format(
            *CURRENT_PYTHON_VERSION, *__required_python_version__
        )
    )
    sys.exit(1)


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="search-engine-api",
    version=__version__,
    python_requires=">={}.{}".format(*__required_python_version__),
    author=__author__,
    author_email=__author_email__,
    description=__description__,
    long_description=__long_description__,
    license="MIT",
    packages=find_packages(),
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")},
    url="https://github.com/RodriguesRodrigo/search-engine-api",
    keywords="Python, Flask, API",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
)
