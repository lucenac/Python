from random import choice
print('Tente adivinhar de 1 à 10 até acertar')

#criando o sorteador
seq = [1,2,3,4,5,6,7,8,9,10]
num = choice(seq)

#entrada
tentativa = int(input('Digite um número de 1 à 10: '))
while tentativa < 1 or tentativa > 10:
    tentativa = int(input('Você deve digititar um número de 1 até 10: '))

cont_tentativas = 1

while tentativa != num:
    cont_tentativas += 1
    tentativa = int(input('Você errou, tente denovo: '))
    while tentativa < 1 or tentativa > 10:
        tentativa = int(input('Você deve digititar um número de 1 até 10: '))

    
print('Parabéns, você o número {} acertou com {} tentavivas!'.format(num, cont_tentativas))