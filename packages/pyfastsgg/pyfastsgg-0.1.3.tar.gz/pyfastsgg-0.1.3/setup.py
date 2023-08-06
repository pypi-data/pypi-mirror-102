# -*- coding: utf-8 -*-
# python 3.8

# # Original version
# from distutils.core import setup, Extension

# Work version
from setuptools import setup, find_packages, Extension


pyfastsgg = Extension('pyfastsgg',
    include_dirs=['./include'],
    sources=[
        './src/Attribute.cpp',
        './src/BufferWriter.cpp',
        './src/DeltaOutDistribution.cpp',
        './src/Distribution.cpp',
        './src/Generation.cpp',
        './src/OutDegreeDistribution.cpp',
        './src/Utility.cpp',
        'c_api.cc'
    ],
    language='c++',
    # extra_compile_args=['-std=c++11']
    extra_compile_args=['-std=c++11', '-fopenmp'],
    extra_link_args=['-lgomp']
)

setup(
    name            = 'pyfastsgg',
    version         = '0.1.3',
    description     = 'Python CXX-API for FastSGG',
    ext_modules     = [pyfastsgg],
    packages        = find_packages()
)
