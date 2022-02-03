class Customer:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self._pin = '123'

	def setPassword(self, new_pin):
		pass

	def verifyPassword(self, pin):
		pass

	def show(self):
		print(f"Client: {self.name} Email: {self.email}")


client1 = Customer('Thiago', 'thiago@email.com')
client2 = Customer('Bruno', 'bruno@email.com')


