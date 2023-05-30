sal = float(input('Digite seu salário:\n'))

if sal >= 1250.0:
    aum = sal + sal * (10/100)
    print('Seu salário agora é de R${}'.format(aum))
    
else:
    aum = sal+ sal * (15/100)
    print('Seu salário agora é de R${}'.format(aum))