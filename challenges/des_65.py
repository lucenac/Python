media = cont = 0
opt = 'S'

while opt != 'N':
    n = int(input('Digite um valor: '))
    cont +=1
    media += n
    if cont == 1:
        maxv = minv = n
    else:
        if n > maxv:
            maxv = n
        if n < minv:
            minv = 1
    opt = str(input('''Quer continuar [S/N] ? ''')).upper().replace(' ','')
        
media = media / cont
print('{} é o maior valor, {} é o menor valor e a média de todos os valores é igual à {:.2f}'.format(maxv,minv,media))