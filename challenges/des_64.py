vf = cont = 0
n = int(input('Digite um valor [999 para parar] : '))
while n != 999:
    vf += n
    cont+=1
    n = int(input('Digite outro valor [999 para parar] : '))
print('Foram mostrado {} números e a soma deles é de {}'.format(cont, vf))