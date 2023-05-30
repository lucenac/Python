vel = float(input('Diga qual a sua velocidade?'))

if vel > 80.0:
    multa1 = vel - 80
    multa2 = multa1 * 7
    print('Você deve pagar R${}'.format(multa2))
    
else:
    print('Você não deve pagar nada')