[![Build Status](https://travis-ci.org/eyalitki/elementals.svg?branch=master)](https://travis-ci.org/eyalitki/elementals) [![Docs Status](https://readthedocs.org/projects/elementals/badge/?version=latest)](https://readthedocs.org/projects/elementals) 

# elementals
Python package with basic utilities for CTF scripts (works well for exploit PoCs too).

## Install
```pip install elementals```

## Read The Docs
https://elementals.readthedocs.io/

## Brief
The **elementals** python package is a utility package with handy tools for CTF scripts and PoC-style scripts. What was first implemented for personal use in small research scripts was now upgraded to be used by security researchers as a lightweight substitute to the famous pwntools package.

The features included in **elementals** are:
* **Logger:** Basic (logging based) logger - configured and ready to use 
* **Prompter:** Metasploit based stdout wrapper for the logger
* **ProgressBar:** User-friendly graphical progress bar
* **StatusBar:** User-friendly graphical status bar
* **createAnchor:** Creates a time-stamped output directory for all script outputs
* **hexDump:** Stylized hex dump for binary blobs / strings

Here is a screenshot from an example script with most of the features:
![Full use case](https://github.com/eyalitki/elementals/blob/master/docs/elementals_poc.png "Full use case")
And here is the log that is stored behind the scenes:
![Stored log](https://github.com/eyalitki/elementals/blob/master/docs/elementals_log.png "Stored log")
Example of the hexDump()'s output:
![Hex dump](https://github.com/eyalitki/elementals/blob/master/docs/elementals_hexdump.png "Hex dump")

## Used by
The **elementals** package is used in most of my scripts and also in my public Github projects:
* **Scout Debugger** - https://github.com/CheckPointSW/Scout
* **Karta (IDA Plugin)** - https://github.com/CheckPointSW/Karta

## References
* E-mail: eyal dot itkin at gmail dot com
