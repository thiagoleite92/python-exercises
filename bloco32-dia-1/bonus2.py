def drawTriangle(n):
	if n <= 0:
		return "Type a number greater than 0"
	count = range(1, n)
	for dot in count:
		print("*" * dot)

drawTriangle(6)
