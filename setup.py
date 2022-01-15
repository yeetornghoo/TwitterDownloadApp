__author__ = "CH"

from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pymongo==4.0"]

setup(
    name="twitterdownloadapp",
    version="0.0.1",
    author="Carlson Hoo",
    author_email="carlson.hoo@gmail.com",
    description="A package Download Tweets from Twitter",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/yeetornghoo/TwitterDownloadApp",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
