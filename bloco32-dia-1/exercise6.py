def isTriangle(*sides):
	for side in sides:
		if side <= 0:
			return "Todos os lados tem que ser maior que 0"
	if sides[0] == sides[1] == sides[2]:
		return "Triângulo equilatero"
	elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
		return "Triângulo isósceles"
	elif sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
		return "Triângulo escaleno"
	else:
		return "Não é triângulo"


print(isTriangle(3, 3, 2))
