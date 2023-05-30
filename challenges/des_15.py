#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

tempo = float(input('Quantos dias você ficou com o carro?\n'))
dist = float(input('Quantos quilometros você rodou no carro?'))

divida = (tempo * 60) + (dist * 0.15)

print('Você deve pagar R${:.2f}'.format(divida))
