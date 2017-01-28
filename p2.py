cur = 0
last = 2
beforeLast = 1

sum = 2

while (cur < 4000000):
	cur = last + beforeLast
	if (cur % 2 == 0):
		sum += cur

	beforeLast = last
	last = cur

print sum