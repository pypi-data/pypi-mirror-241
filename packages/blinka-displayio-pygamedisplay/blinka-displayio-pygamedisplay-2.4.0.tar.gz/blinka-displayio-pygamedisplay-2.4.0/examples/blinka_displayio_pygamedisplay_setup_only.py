# SPDX-FileCopyrightText: 2020 Tim C
#
# SPDX-License-Identifier: Unlicense
"""
Make green and purple rectangles and a
"Hello World" label.
"""
import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay


# Make the display context. Change size if you want
display = PyGameDisplay(width=320, height=240)

# Make the display context
main_group = displayio.Group()
display.show(main_group)


while True:
    if display.check_quit():
        break
