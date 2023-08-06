gewel-btchip-python
====================

Python communication library for Ledger Hardware Wallet products (Gewel fork)

Requirements
-------------

This library requires libusb-1.0-0-dev, libudev-dev, python2.7-dev and wheel for building. On Debian systems:

```sh
sudo apt-get install libusb-1.0-0-dev libudev-dev python2.7-dev
pip install wheel
```

The library can then be installed via pip:

```sh
pip install gewel-btchip-python
```

For optional BIP 39 support during dongle setup, also install https://github.com/trezor/python-mnemonic - also available as a Debian package at the previous link (python-mnemonic)

Building on Windows
--------------------

  - Download and install the latest Python 2.7 or 3.x version from https://www.python.org/downloads/windows/
  - Install Microsoft Visual C++ Compiler for Python 2.7 or 3.x from http://www.microsoft.com/en-us/download/details.aspx?id=44266
  - Download and install PyQt4 for Python 2.7 or 3.x from https://www.riverbankcomputing.com/software/pyqt/download
  - Install the gewel-btchip library (open a command prompt and enter c:\python27\scripts\pip install gewel-btchip-python)
