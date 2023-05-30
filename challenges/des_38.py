num_1 = int(input('Digite um número inteiro:\n'))
num_2 = int(input('Dugite outro número inteiro:\n'))

if num_1 > num_2:
    print('O numéro {} é maior que o número {}!'.format(num_1, num_2))
    
elif num_2 > num_1:
    print('O numéro {} é maior que o número {}!'.format(num_2, num_1))
    
else:
    print('Os números são iguais!')