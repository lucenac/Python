#crie um programa que leia a data de nascimento de sete pessoas> No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
ano = date.today().year

countmaior = 0
countmenor = 0

for c in range(0,7):
    data = int(input('Digite a data de nascimento da pessoa {}: '.format(c + 1)))
    if data <= ano - 18:
        countmaior+=1
    else:
        countmenor+=1
        
print('{} pessoas são de maior e {} são de menor'.format(countmaior, countmenor))