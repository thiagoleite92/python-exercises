class Rectangle:
	def __init__(self, height, width):
		self.height = height
		self.width = width

	def squares(self):
		print(self.height * self.width)

	def perimeter(self):
		print(2 * (self.height * self.width))

first_rectangle = Rectangle(10, 10)
second_rectangle = Rectangle(10, 20)


first_rectangle.squares()
first_rectangle.perimeter()

second_rectangle.squares()
second_rectangle.perimeter()
