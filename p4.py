# find the larest palindromic # that's the product of two 3-digit numbers

def is_palindrome(num):

	num = list(str(num))
	reverse = num[::-1]

	if num == reverse:
		return True
	else:
	    return False

def run():

	highest_num = 0
	for x in reversed(range(0, 999)):
		for y in reversed(range(0, 999)):
			num = x*y
			if is_palindrome(num) & (num > highest_num):
				highest_num = num

	print highest_num

run()



