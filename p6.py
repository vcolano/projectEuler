# difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum

nums = list(range(1, 101))

sum_of_squares = 0
sum_of_nums = 0
for num in nums:
	sum_of_squares += num*num
	sum_of_nums += num

square_of_sum = sum_of_nums*sum_of_nums

print str( square_of_sum - sum_of_squares)


