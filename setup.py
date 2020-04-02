from setuptools import setup
import versioneer

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="my_pkg",
    version=versioneer.get_version(),
    description="My package",
    author="Curtis Hampton",
    author_email="CurtLHampton@gmail.com",
    packages=["my_pkg"],
    install_requires=requirements,
    entry_points={"console_scripts": ["my_pkg=my_pkg.cli:my_pkg",],},
    extras_require={"dev": ["pytest", "sphinx", "sphinxcontrib-napoleon"]},
    keywords="my_pkg",
    classifiers=["Programming Language :: Python :: 3.6", "Programming Language :: Python :: 3.7",],
)
