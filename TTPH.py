#!/usr/bin/python
from sense_hat import SenseHat
sense = SenseHat()

r = (128, 0, 0)
g = (0, 128, 0)
b = (0, 0, 128)

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()

  t = (t * 9 / 5 + 32)#convert C to F
  p = (p / 33.864)#convert millibars to inHg

  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 2)
  h = round(h, 1)
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
  
  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05, text_colour = g )
