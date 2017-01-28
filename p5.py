# smallest number evenly divisible by all numbers in [1, 2, ..., 20]

num_not_found = True

num = 0
while num_not_found:
	num += 20
	divisible = True
	for x in range(1, 21):
		if (num % x) != 0:
			divisible = False
			break

	if divisible:
		print str(num)
		num_not_found = False
