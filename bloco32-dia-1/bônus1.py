numbers = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]

def minorNumber(listNumbers):
	minor = listNumbers[0]
	for number in listNumbers:
		if number < minor:
			minor = number
	return minor


print(minorNumber(numbers))
