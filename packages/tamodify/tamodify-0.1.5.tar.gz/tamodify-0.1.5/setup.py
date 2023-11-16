#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools,distutils,shutil,re,os
from distutils.core import setup, Extension

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

module1 = Extension('tamodify',
    define_macros = [('MAJOR_VERSION', '1'),
        ('MINOR_VERSION', '0')],
    include_dirs = ['src'],
    sources = ['src/tamodify.c','src/tajk_data2.c','src/tajk_modify.c','src/tajk_lib.c']
)

setuptools.setup(
    name="tamodify",
    version="0.1.5",
    author="Chen chuan",
    author_email="13902950907@139.com",
    description="TA接口文件修改",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://gitee.com/chenc224/ofbdep/tree/master/python",
    python_requires='>=3.5',
    zip_safe= False,
    include_package_data = True,
    ext_modules = [module1],
#    package_dir={"":"datafile"},
#    package_data={"":["*"]},
    data_files=[('tamodify', ['datafile/t.py'])],
)
