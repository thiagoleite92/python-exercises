import math

class Circle():
	def __init__(self, diametro):
		self.diametro = diametro
		self.raio = diametro / 2
		self.PI = math.pi

	def calcularArea(self):
		print(self.PI * (math.sqrt(self.raio)))

	def showInfo(self):
		print(f"Diamentro: {self.diametro}, Raio: {self.raio} ")

	def calcPerimetro(self):
		print(f"{2 * self.PI* self.raio:0.2f}")


circle_1 = Circle(2)

circle_1.calcularArea()
circle_1.showInfo()
circle_1.calcPerimetro()
