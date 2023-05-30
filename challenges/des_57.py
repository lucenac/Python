sexo = str(input('Qual o seu seo [M/F]?\n ')).upper().replace(' ','')

while sexo != 'M' and sexo != 'F':
    print('Parece que você digitou errado!')
    sexo = str(input('Qual o seu seo [M/F]?\n '))
    
print('Você é {}'.format(sexo))