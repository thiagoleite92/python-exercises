names = ["Francisco", "José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana", "Sebastiao"]

def biggerName(nomes):
	greaterName = []

	nameLength = 0

	for name in nomes:
		if len(name) >= nameLength:
				nameLength = len(name)
				greaterName.append(name)

	return greaterName


print(biggerName(names))
