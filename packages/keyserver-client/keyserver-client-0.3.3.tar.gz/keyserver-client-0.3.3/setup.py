# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="keyserver-client",
    version="0.3.3",
    description="Client for the RG Keyserver",
    author="Kevin McCarthy",
    author_email="kevin@realgeeks.com",
    url="https://github.com/realgeeks/keyserver_client",
    packages=find_packages(exclude=("tests", "docs")),
    entry_points={
        "console_scripts": ["keyserver-client=keyserver_client.command_line:main"]
    },
)
