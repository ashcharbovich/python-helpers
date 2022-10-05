# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='helpers',
    version='0.1.0',
    description='Python Helpers Funcs',
    long_description=readme,
    python_requires=">=3.9",
    packages=['python-helpers'],
    install_requires=['psycopg2'],
)
