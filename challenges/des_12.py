valor = float(input('Digite um valor:\nR$'))

desc = valor - valor * (5 / 100)

print('R${} com 5% de desconto é igual à R${}'.format(valor, desc))