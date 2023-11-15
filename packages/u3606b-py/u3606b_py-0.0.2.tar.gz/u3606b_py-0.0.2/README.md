[![Build and Publish](https://github.com/leeebo/u3606b_py/actions/workflows/release_to_pypi.yml/badge.svg)](https://github.com/leeebo/u3606b_py/actions/workflows/release_to_pypi.yml) [![version](https://img.shields.io/pypi/v/u3606b_py)](https://pypi.python.org/pypi/u3606b_py) [![license](https://img.shields.io/pypi/l/u3606b_py)](https://pypi.python.org/pypi/u3606b_py) 

## u3606b Python driver (unofficial)

This is a Python driver for the u3606b multimeter. It is based on the official [U3606B Multimeter| DC Power Supply Programming Guide](https://www.keysight.com/us/en/assets/9018-03963/programming-guides/9018-03963.pdf) and PyVISA package. [PyVISA](https://pyvisa.readthedocs.io/projects/pyvisa-py/en/latest/) is a Python package that allows you to control measurement devices independently of the interface (GPIB, USB, Ethernet, etc.) by using a common API.

The driver is not complete, but it is a good starting point for anyone who wants to control the u3606b multimeter with Python.

The driver supports the following functions:

* Read voltage
* Read current
* Set voltage
* Set current
* Set output on/off
* Set limits
* Step output

## Pre-requisites

* Python 3.8 or higher (lower versions may work, but have not been tested)
* Windows: [NI-VISA](https://www.ni.com/zh-cn/support/downloads/drivers/download.ni-visa.html#494653) or [NI-488.2](https://www.ni.com/zh-cn/support/downloads/drivers/download.ni-488-2.html#305442) or [Keysight IO Library Suite](https://www.keysight.com/en/pd-1985909/io-libraries-suite/)
* Linux/MAC: please refer to [gpib-resources-gpib-instr](https://pyvisa.readthedocs.io/projects/pyvisa-py/en/latest/installation.html#gpib-resources-gpib-instr)

## Installation

```bash
pip install u3606b_py
```

## Example

```python
from u3606b_py.u3606b import U3606B

u3606b_dev = U3606B()
u3606b_dev._open()
u3606b_dev._reset()
u3606b_dev.sour_vol_rng(rng='8V')
u3606b_dev.sour(lvl='1.0V')
```
