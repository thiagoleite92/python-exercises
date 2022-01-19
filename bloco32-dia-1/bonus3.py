def sumDigits(n):
	sum_digits = 0
	count = range(1, n + 1)
	for number in count:
		sum_digits += number
	return sum_digits

print(sumDigits(5))
