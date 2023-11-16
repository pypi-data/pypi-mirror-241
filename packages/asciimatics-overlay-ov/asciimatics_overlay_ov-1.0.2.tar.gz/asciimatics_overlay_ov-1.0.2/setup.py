"""
File containing the required information to successfully build a python package
"""

import setuptools

with open("README.md", "r", encoding="utf-8", newline="\n") as fh:
    long_description = fh.read()

setuptools.setup(
    name='asciimatics_overlay_ov',
    version='1.0.2',
    packages=setuptools.find_packages(),
    install_requires=[
        "asciimatics==1.14.0",
        "english-words==2.0.1",
        "python-magic==0.4.7"
    ],
    author="Henry Letellier",
    author_email="henrysoftwarehouse@protonmail.com",
    description="A module that help speed up some elements in using asciimatics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hanra-s-work/asciimatics_overlay_ov",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
