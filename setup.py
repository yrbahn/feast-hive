# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

INSTALL_REQUIRE = [
    "feast>=0.12.0",
    "pyhive==0.6.3",
]

TEST_REQUIRE = ["pytest==6.0.0"]

DEV_REQUIRE = [
    "flake8",
    "black==19.10b0",
    "isort>=5",
    "mypy==0.790",
]

setup(
    name="feast-hive",
    version="0.1",
    author="Benn Ma",
    author_email="bennmsg@gmail.com",
    description="Hive support for Feast offline store",
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">=3.7.0",
    url="https://github.com/baineng/feast-hive",
    license=license,
    packages=["feast_hive"],
    install_requires=INSTALL_REQUIRE,
    extras_require={
        "dev": DEV_REQUIRE + TEST_REQUIRE,
        "test": TEST_REQUIRE,
    },
    keywords=("feast featurestore hive offlinestore"),
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
