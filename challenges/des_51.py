pa = int(input('Qual o valor da PA: '))
r = int(input('Qual a razão: '))

p = 10 * r

for c in range(pa, p, r):
    print('{} ->'.format(c), end=" ")
    
print('ACABOU!')        