import random

print('Tente adivinhar de 0 à 5!')
seq = [0, 1, 2, 3, 4, 5]
num = random.choice(seq)

cnum = int(input('Digite seu número: '))

print('Eu pensei no número {}'.format(cnum))

if num == cnum:
    print('Parabéns, você acertou')
    
else:
    print('Que pena, você errou!')