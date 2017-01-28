
import sys
import math

for a in range(0, 500):
	for b in range(0, a):
		c = math.sqrt(math.pow(a,2)+math.pow(b,2))
		# print "c: " + str(c)
		# print "a+c+c: " + str(a+b+c)
		if (a+b+c) == 1000:
			print str(a*b*c)
		#print "a: " + str(a) + "    " + "b: " + str(b)
