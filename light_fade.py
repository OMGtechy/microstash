"""
    This file is part of microstash.

    microstash is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    microstash is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with microstash.  If not, see <http://www.gnu.org/licenses/>.
"""

from microbit import *

def wave():
    image = Image('99999:99999:99999:99999:99999:')
    last_pixel = (-1, -1)

    a_pixel_is_on = True
    pixel_changed = True

    def degrade(image, x, y):
	current = image.get_pixel(x, y)
	if current > 0:
	    pixel_changed = True
	    image.set_pixel(x, y, current - 1)

    while a_pixel_is_on:
	a_pixel_is_on = False
	pixel_changed = False
	degrade_even_x = False
	degrade_even_y = False

	for y in range(5):
	    for x in range(5):
		current = image.get_pixel(x, y)

		if (x % 2 == 0) and (current > 0):
		    degrade_even_x = True

		if (x % 2 != 0) and (current > 0):
		    degrade_even_y = True

		if current > 0:
		    a_pixel_is_on = True

		if (((degrade_even_x and x % 2 == 0) or
		     (degrade_even_y and y % 2 == 0)) or
		    (((not degrade_even_x) and x % 2 != 0) or
		     ((not degrade_even_y) and y % 2 != 0))):
		    degrade(image, x, y)

	yield image

sleep_time = 50

while True:
    for stage in wave():
	display.show(stage)

	if button_a.was_pressed():
	    sleep_time -= 1

	if button_b.was_pressed():
	    sleep_time += 1

	if sleep_time < 0:
	    sleep_time = 0

	sleep(sleep_time)

