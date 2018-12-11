from setuptools import setup, find_packages
from codecs     import open
from os         import path

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='elementals',
      version='1.2.2',
      description='Basic utilities for CTF (or exploit) scripts',
      author='Eyal Itkin',
      author_email='eyal.itkin@gmail.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/eyalitki/elementals',
      license='GPL',
      packages=find_packages(exclude=['tests']),
      install_requires=['colorama', 'hexdump'],
      classifiers=[
                    "Programming Language :: Python",
                    "License :: OSI Approved :: GNU General Public License (GPL)",
                    "Operating System :: OS Independent",
                  ],
      zip_safe=False)
