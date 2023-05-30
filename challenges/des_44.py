valor = float(input('Qual o valor? '))
fp = int(input('''Qual a forma de pagamento?
    1-À vista no dinheiro ou pix
    2-À vista no cartão
    3-2x no cartão
    4-3x ou mais no cartão
Digite um valor: '''))

if fp == 1:
    desc = valor - (valor * (10/100))
    print('Você deve pagar R${:.2}'.format(desc))
    
elif fp == 2:
    desc = valor - (valor * (5/100))
    print('Você deve pagar R${:.2}'.format(desc))
    
elif fp == 3:
    print('Você deve pagar R${:.2}'.format(valor))
    
elif fp ==4:
    desc = valor + (valor * (20/100))
    print('Você deve pagar R${:.2}'.format(desc))
    
else:
    print('Você escolheu uma opção não existente...')
    