# OpenOCD Plug
[![Build Status](https://travis-ci.org/jo-nas/openocd_plug.svg?branch=master)](https://travis-ci.org/jo-nas/openocd_plug) [![Coverage Status](https://coveralls.io/repos/github/jo-nas/openocd_plug/badge.svg?branch=master)](https://coveralls.io/github/jo-nas/openocd_plug?branch=master)  
This Plug can handle basic commands from OpenOCD.

## Installation
To install the plug you can use PIP:
```bash
pip install git+https://github.com/jo-nas/openocd_plug.git
```

## Usage

Flash a firmware:
```python
import openhtf
from openocd_plug import OpenOCDPlug

@openhtf.plug(ocd=OpenOCDPlug)
def flash_firmware_example(test, ocd):
    ocd.programm("firmware_file.hex")
```

## Requirements
- [openhtf](https://github.com/google/openhtf): The open-source hardware testing framework.

## Authors
*openocd_plug* was written by *Jonas Steinkamp<jonas@steinka.mp>*.
