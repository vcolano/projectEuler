import math

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors

def num_factors(n):
	"""Returns the number of factors of n using the Tau function"""
	p_factors = prime_factors(n)
	num = 1

	# iterate through unique items in p_factors
	for f in list(set(p_factors)):
		num *= (p_factors.count(f) + 1)

	return num



found = False
num = 1
tri_num = 1
while not found:
	f = num_factors(tri_num)
	if f < 500:
		num += 1
		tri_num += num
	else:
		found = True
		print str(tri_num)