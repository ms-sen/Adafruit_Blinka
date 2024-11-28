# SPDX-FileCopyrightText: 2024 Maxine Shefkiu
#
# SPDX-License-Identifier: MIT
"""Pin definitions for the BeaglePlay"""

from adafruit_blinka.microcontroller.am625x import pin
# incomplete, will only work with qwiic i2c port
P17 = pin.P17
P18 = pin.P18

SDA = P18
SCL = P17
