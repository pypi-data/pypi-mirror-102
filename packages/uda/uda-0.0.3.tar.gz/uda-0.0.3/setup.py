# !/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name='uda',
    version='0.0.3',
    author='memory shen',
    author_email='zhengyang.shen@ipp.ac.cn',
    description=u'uda python client lib',
    license="MIT",
    packages=find_packages(),
    url='https://packaging.python.org/',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
            'numpy>=1.19.2'
    ],
)