sum = 0
for x in range(0,1000):
	if x%5 == 0:
		sum += x
	elif x%3 == 0:
		sum +=x

print str(sum)