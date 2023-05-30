while True:
    cont = 0
    n = int(input('Você quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*50)
    while cont < 10:
        cont+=1
        op = n * cont
        print(f'{n} x {cont} = {op}')
    print('-'*50)
print('Programa encerrado!')