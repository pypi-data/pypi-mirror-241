from setuptools import setup, find_packages


# Fix for older setuptools
import re
import os

from demo_multiply import __version__
from demo_multiply import __author__


# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()



file_text = read(fpath('demo_multiply/__init__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


# This call to setup() does all the work
setup(
    name="demo-multiply",
    version=grep('__version__'),
    description="Demo library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author=grep('__author__'),
    author_email="example@email.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python',
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    packages=["demo_multiply"],
    include_package_data=True,
    install_requires=[]
)