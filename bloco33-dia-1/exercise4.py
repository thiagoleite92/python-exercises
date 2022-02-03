class Order():
	def __init__(self, order, quantity, customer):
		self.order = order
		self.quantity = quantity
		self.customer = customer
		self.full_price = quantity * order
		self.total_price = self.calcDiscount()
		self.discount = self.validDiscount()


	def validDiscount(self):
		if self.total_price >= 50:
			self.discount = True
			return self.discount
		else:
			self.discount = False
			return self.discount

	def calcDiscount(self):
		if 50 >= self.full_price < 75:
			self.total_price = self.full_price * 0.90
			return self.total_price
		elif 75 < self.full_price <= 90:
			self.total_price = self.full_price * 0.85
			return self.total_price
		elif 90 < self.full_price <= 100:
			self.total_price = self.full_price * 0.82
			return self.total_price
		elif self.full_price > 100:
			self.total_price = self.full_price * 0.80
			return self.total_price
		else:
			return self.full_price

order_1 = Order(10, 11, 'Thiago')

print(order_1.total_price)
