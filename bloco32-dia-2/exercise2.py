import random
chances = 0

words_list = ['thiago', 'josé', 'siqueira', 'leite']

word = random.choice(words_list)

scrambled_word = "".join(random.sample(word, len(word)))

print("scrambled_word: " + scrambled_word)
answer = input("guess the word: ")

while answer != word or chances < 5:
	if answer == word:
		print("Você acertou!" + answer)
		break
	elif chances == 2:
		print('Acabaram as chances')
		break
	answer = input("guess the word")
	chances += 1

