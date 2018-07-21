from setuptools import setup, find_packages
from codecs import open
from os import path

setup(name='elementals',
      version='0.9',
      description='Basic utilities for CTF scripts',
      author='Eyal Itkin',
      author_email='eyal.itkin@gmail.com',
      license='GPL',
      packages=find_packages(exclude=['tests']),
      install_requires=['colorama'],
      zip_safe=False)
