
def collatz(n):
	"""returns the number of steps in the collatz sequence for int n"""
	global counter
	counter += 1
	if n == 1:
		return
	if n%2 == 0:
		collatz(n/2)
	elif n%2 == 1:
		collatz(n*3+1)

longest_sequence = 0
longest = -1
for x in range(2, 1000000):
	counter = 0
	collatz(x)
	print (str(x))
	if counter > longest_sequence:
		longest_sequence = counter
		longest = x

print("longest sequence is " + str(longest_sequence) + " from number " + str(longest))