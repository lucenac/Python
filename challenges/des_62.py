print('Gerador de PA')
print('-='*30)

#entrada
pa= int(input('Digite o valor da PA: '))
r = int(input('Digite o valor da razão: '))
t = pa
cont = 1
cont_t = 0

#10 termos iniciais 
while cont <= 10:
    print('{} → '.format(t), end='')
    t+=r
    cont+=1
    cont_t+=1
print('Fim')

#termos variáveis
tp = 1
while tp > 0:
    tp = int(input('Quantos termos você quer a mais?'))
    cont = 1

    if tp > 0:
        while cont <= tp:
            print('{} → '.format(t), end='')
            t+=r
            cont+=1
            cont_t+=1
    print('Fim')
print('Fim da progressão com {} termos.'.format(cont_t))