cont = soma = 0
while True: 
    n = int(input('Digite um valor (999 para sair): '))
    if n == 999:
        break
    cont+=1
    soma += n
print(f'O número apareceu {cont} vezes e a soma entre eles é de {soma}')
    