# find the 10,001st prime number

primes = [2]

num = 3

while len(primes) < 10001:

	num_is_prime = True
	for prime in primes:
		if num%prime is 0:
			num_is_prime = False
			break

	if num_is_prime:
		primes.append(num)

	num += 1

print str(primes[len(primes) - 1])

