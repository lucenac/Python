#crie um programa que leia uma frase e diga se ela é não é um palindromo, desconciderando os espaços
#apos a sopa

frase = str(input('Digite a frase:')).lower().replace(' ','')
if frase == frase[::-1]:
    print('A frase é um palíndromo!')
    
else:
    print('A frase não é um palindromo!')