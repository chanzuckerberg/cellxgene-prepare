#!/usr/bin/env python

from setuptools import setup

version = '1.0.0'

required = open('requirements.txt').read().split('\n')

setup(
    name='cellxgene-prepare',
    version=version,
    description=' ',
    author='freeman-lab',
    author_email='the.freeman.lab@gmail.com',
    url='https://github.com/chanzuckerberg/cellxgene-prepare',
    packages=['prepare'],
    install_requires=required,
    long_description='See ' + 'https://github.com/chanzuckerberg/cellxgene-prepare',
    license='MIT'
)
