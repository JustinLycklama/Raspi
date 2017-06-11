#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-17 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Simple println capabilities.
"""

import os
import time
import sys
from datetime import datetime
from pytz import timezone
from demo_opts import get_device
from luma.core.virtual import terminal
from darksky import forecast

def make_font(name, size):
	font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fonts', name))
	return ImageFont.truetype(font_path, size)

def main():
		font = None
		term = terminal(device, font, animate=False)

		term.println("")
		term.println(" Loading ...")

		key = "341d16f1681516644dff755d27b202e9"
		lat = 43.647513
		long = -79.392702

		toronto = forecast(key, lat, long, units="si", exclude="minutely,hourly,alerts,flags") 

		term.clear()

		daily = toronto.daily[0]

		localTimeZone = timezone('America/Toronto')
		localTime = datetime.now(localTimeZone)
		dayString = localTime.strftime('%A %B %d')

		term.println("  " + dayString)
 		term.println("-------------------")
			
		current = "    " + str(int(toronto.temperature))
		current += " (" + str(int(toronto.apparentTemperature)) + ") - "
		current += str(int(daily.precipProbability * 100)) + "%"


		term.println(current)

		high = " "
		high += str(int(daily.temperatureMax)) + " ("
		high += str(int(daily.apparentTemperatureMax)) + ")"
		
		high += " - " +  str(int(daily.temperatureMin)) + " ("
		high += str(int(daily.apparentTemperatureMin)) + ")"

		term.println(high)

		# Info By Hour
		#hourly = toronto.hourly()
		#hour = -1
		#displayHours = [10, 13, 16, 19, 22]
		#temps = ""
		#percips = ""
		#for dataPoint in hourly.data:
			#hour += 1
			#if hour not in displayHours:
				#continue

			#temps += str(dataPoint.temperature)
			#percips += str(dataPoint.percipProbability)

		#term.println(temps)		  
		#term.println(percips)		  

 		time.sleep(25)
		sys.exit()

if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
