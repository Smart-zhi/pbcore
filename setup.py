#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from setuptools import setup, find_packages

import sys
import os

if sys.version_info[0:2] != (2, 7):
    print('pbcore requires Python 2.7')
    sys.exit(-1)

test_deps = [
    'coverage',
    'pytest',
    'pytest-cov',
    'pytest-xdist',
    'pyxb == 1.2.4',
    'sphinx',
    'pylint == 1.6.4',
]

setup(
    name='pbcore',
    version='1.8.1', # don't forget to update pbcore/__init__.py and doc/conf.py too
    author='Pacific Biosciences',
    author_email='devnet@pacificbiosciences.com',
    description='A Python library for reading and writing PacBio® data files',
    license='BSD-3-Clause-Clear',
    packages=find_packages(),
    include_package_data=True,
    exclude_package_data={'pbcore.data': ['Makefile']},
    zip_safe=False,
    entry_points={'console_scripts': ['.open = pbcore.io.opener:entryPoint']},
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
        'future >= 0.16.0',
        'numpy >= 1.7.1',
        'pysam >= 0.15.1',
    ],
    test_requires=test_deps,
    extras_require={'test': test_deps},
)
