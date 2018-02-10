'''
-Python Calculator(without functions) By Damian-
Python is especially useful for doing math and can be used to automate many calculations.

This program can compute the area of a given shape, as selected by the user. The calculator will be able to determine the area of the following shapes:
	-Circle
	-Triangle
'''
from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print "Welcome to Shape Area Calculator!"
print '%s/%s/%s %s:%s' % (now.month, now.day, now.year, now.hour, now.minute)

#Sleeping a program is not common practice. I am using it to simulate a thinking calculator.
sleep(1)

hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle:")
option = option.upper()

if option == 'C':
  radius = float(raw_input("Enter the radius:"))
  area = (pi * (radius ** 2))
  print "The pie is baking..."
  sleep(1)
  print "%.2f\n%s" % (area, hint)
elif option == 'T':
  base = float(raw_input("Enter the base:"))
  height = float(raw_input("Enter the height:"))
  area = (base * height)/2
  print "Uni Bi Tri..."
  sleep(1)
  print "%.2f\n%s" % (area, hint)
else:
  print "Incorrect shape type entered...\nExiting..."
