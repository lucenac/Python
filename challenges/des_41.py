data = int(input('Qual o ano que você nasceu?'))

idade = 2023 - data

if  idade <= 9:
    print('Mirim')
    
elif idade <= 14:
    print('Infantil')
    
elif idade <= 19:
    print('Junior')
    
elif idade <= 20:
    print('Sênior')
    
else:
    print('Master')