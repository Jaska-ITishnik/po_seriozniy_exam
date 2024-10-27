from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        '',
        ['c.cpp'],
        include_dirs=[pybind11.get_include()],
    ),
]

setup(
    name='example',
    ext_modules=ext_modules,
)
