def greatNumber(*number):
    print(f'Meu primeiro número é {number[0]}, e meu segundo número é {number[1]}')
    if number[0] > number[1]:
        return number[0]
    else:
      return number[1]

print(greatNumber(200, 300)) 
