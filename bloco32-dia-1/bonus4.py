#   Álcool:
#     - Até 20 litros, desconto de 3% por litro;
#     - Acima de 20 litros, desconto de 5% por litro.
#   Gasolina:
#     - Até 20 litros, desconto de 4% por litro;
#     - Acima de 20 litros, desconto de 6% por litro."
#	gasolina custa 2,50
#	alcool custa 1,90
#

def refuel(fuel, quantity):
	alcool_price = 1.90
	gasoline_price = 2.50

	if fuel == "A" and quantity <= 20:
		return quantity * alcool_price * 99.7
	elif fuel == "A" and quantity > 20:
		return quantity * alcool_price * 99.5
	elif fuel == "G" and quantity <= 20:
		return (quantity * quantity * 99.6)
	elif fuel == "G" and quantity > 20:
		return (quantity * gasoline_price * 0.06)
	else:
		return "Dados não reconhecidos" ## meu cṕdigo


# print(refuel("G", 20))

# def fuel_price(type, liters):
#     if type == "A":
#         price = 1.90
#         discount = 0.03
#         if liters > 20:
#             discount = 0.05
#     elif type == "G":
#         price = 2.50
#         discount = 0.04
#         if liters > 20:
#             discount = 0.06
#     total = price * liters
#     total -= total * discount
#     return total

# print(fuel_price("G", 20)) gabarito
