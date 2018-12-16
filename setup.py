from setuptools import setup, find_packages
from codecs     import open
from os         import path

# Different from the README.md, because PyPi struggles with shwoing PNG images
long_description = '''# elementals
Python package with basic utilities for CTF scripts (works well for exploit PoCs too).

## Install
```pip install elementals```

## Read The Docs
https://elementals.readthedocs.io/

## Github
https://github.com/eyalitki/elementals

## Brief
The **elementals** python package is a utility package with handy tools for CTF scripts and PoC-style scripts. What was first implemented for personal use in small research scripts was now upgraded to be used by security researchers as a lightweight substitute to the famous pwntools package.

The features included in **elementals** are:
* **Logger:** Basic (logging based) logger - configured and ready to use 
* **Prompter:** Metasploit based stdout wrapper for the logger
* **ProgressBar:** User-friendly graphical progress bar
* **StatusBar:** User-friendly graphical status bar
* **createAnchor:** Creates a time-stamped output directory for all script outputs
* **hexDump:** Stylized hex dump for binary blobs / strings

## Used by
The **elementals** package is used in most of my scripts and also in my public Github projects:
* **Scout Debugger** - https://github.com/CheckPointSW/Scout
* **Karta (IDA Plugin)** - (soon to be released)

## References
* Twitter: [@EyalItkin](https://twitter.com/EyalItkin)
* E-mail: eyal dot itkin at gmail dot com'''

setup(name='elementals',
      version='1.2.3',
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
