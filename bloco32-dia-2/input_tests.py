import random, sys

# user_name = input("Digite seu nome:")

# print(f"seu nome é: {user_name}")

# random_number = random.randint(1, 10)

# guess = ""

# while guess != random_number:
# 	guess = int(input("qual o seu palpite? "))

# print(f"O número sorteado foi: {guess}")

if __name__ == "__main__":
	for argument in sys.argv:
		print("received -> ", argument )
