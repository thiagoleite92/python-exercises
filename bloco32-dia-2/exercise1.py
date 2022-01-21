user_name = input('Type your name: ')

counter = len(user_name)

while counter > 0:
	print(user_name[0:counter])
	counter += -1

