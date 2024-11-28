# SPDX-FileCopyrightText: 2024 Maxine Shefkiu
#
# SPDX-License-Identifier: MIT
"""TI AM625x pin names"""
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

# i2c qwiic only, incomplete
P17 = None
P18 = None

I2C5_SCL = P17
I2C5_SDA = P18

i2cPorts = ((5, I2C5_SCL, I2C5_SDA),)
