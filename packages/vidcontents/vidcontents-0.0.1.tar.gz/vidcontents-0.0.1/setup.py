from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A ContentsManager for managing Google Cloud APIs.'
LONG_DESCRIPTION = 'A package that allows to build a contents manager for jupyter applications.'

# Setting up
setup(
    name="vidcontents",
    version=VERSION,
    author="Sanskar Jain",
    author_email="sanskarj123@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "notebook>=6.0.0", 
        "nbformat>=5.0.0",
        "tornado>=6", 
        "traitlets>=5.0.0"
        ],
    keywords=['python', 'jupyter', 'contents manager'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
