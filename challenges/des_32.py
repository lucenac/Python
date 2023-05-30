ano = int(input('Digite um ano:'))
anobi = ano % 4

if anobi == 0:
    print('Esse ano é bissexto')
    
else:
    print('Esse ano não é bissexto')