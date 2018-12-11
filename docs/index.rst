.. elementals documentation master file, created by
   sphinx-quickstart on Tue Dec 11 22:03:02 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to elementals's documentation!
======================================

Brief
-----
The **elementals** python package is a utility package with handy tools for CTF scripts and PoC-style scripts. What was first implemented for personal use in small research scripts was now upgraded to be used by security researchers as a lightweight substitute to the famous pwntools package.

``pip install elementals``

The features included in **elementals** are:

* **Logger:** Basic (logging based) logger - configured and ready to use 
* **Prompter:** Metasploit based stdout wrapper for the logger
* **ProgressBar:** User-friendly graphical progress bar
* **StatusBar:** User-friendly graphical status bar
* **createAnchor:** Creates a time-stamped output directory for all script outputs
* **hexDump:** Stylized hex dump for binary blobs / strings

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   Logger
   Prompter
   ProgressBar
   StatusBar
   createAnchor
   hexDump

Used by
----------
The **elementals** package is used in most of my scripts and also in my public Github projects:

* **Scout Debugger** - https://github.com/CheckPointSW/Scout
* **Karta (IDA Plugin)** - (soon to be released)

References
--------------

* Github repository: https://github.com/eyalitki/elementals
* Twitter: https://twitter.com/EyalItkin
* E-mail: eyal dot itkin at gmail dot com