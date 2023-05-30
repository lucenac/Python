dist = float(input('Qual a distância da sua viagem?\n'))

if dist >= 201:
    valor = dist * 0.45
    print('Você deve pagar R${}'.format(valor))
    
else:
    valor = dist * 0.5
    print('Você deve pagar R${}'.format(valor))
    