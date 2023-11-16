from setuptools import Extension, setup

ext = Extension(
    name='meshset',
    sources=['meshset.cpp'],
)

setup(
    name='meshes',
    version='0.1.0',
    ext_modules=[ext],
)
