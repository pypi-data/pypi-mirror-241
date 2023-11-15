# coding=utf-8

from setuptools import setup
# from distutils.core import setup
# from distutils.core import Distribution
# Distribution.has_ext_modules = lambda *args, **kwargs: True
from pathlib import Path
import os, sys, subprocess

subprocess.run("rm -rf ./build tr.egg-info", shell=True)
                            

appname = "ort"
version = "1.0.1"

try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
except:
    readme = ""

packages = ["ort"]

setup(
    name=appname,
    version=version,
    description=(
        '''%s''' % appname
    ),

    author='anycode',
    author_email='anycode@yahoo.com',
    maintainer='anycode',
    maintainer_email='anycode@yahoo.com',
    packages=packages,
    platforms="linux",
    url='https://pypi.org/project/%s/' % appname,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
    ],
    # package_data = {
    #     '': ['*.dll', "crnn.bin", "*.txt"],
    # },
    include_package_data=True,

    long_description=readme,
    long_description_content_type='text/markdown'
)
