#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
	x = 'is negative'
else if number == 0:
	x = 'is zero'
else:
	x = 'is positive'
print (number + ' ' + x)
