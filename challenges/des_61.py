print('Gerador de PA')
print('-='*30)
pa= int(input('Digite o valor da PA: '))
r = int(input('Digite o valor da razão: '))
t = pa
cont = 1

while cont <= 10:
    print('{} → '.format(t), end='')
    t+=r
    cont+=1
print('Fim')