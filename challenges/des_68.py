from random import choice

print('Par ou Ímpar')
print('-'*30)
while True:
    cpu = [1,2,3,4,5,6,7,8,9,10]
    cpu_c = choice(cpu)
    v = int(input('Diga um valor: '))
    pi = str(input('Você quer par ou impar? [P/I] ')).upper().replace(' ','')
    soma = v + cpu_c
    print('-'*30)
    print(f'Você jogou {v} e o cpu jogou {cpu_c}, que é igual à {soma}')
    print('-'*30)
    if pi == 'P':
        if soma %2 == 0:
            print('Você venceu!')
            print('Vamos jogar novamente...')
        else:
            print('Você perdeu!')
            break
    if pi == 'I':
        if soma %2 == 0:
            print('Você perdeu!')
            break
        else:
            print('Você venceu!')
            print('Vamos jogar novamente...')

