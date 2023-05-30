n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Agora outro número: '))

if n1 > n2 and n1 > n3:
    print('{} é o mair número'.format(n1))
    
elif n2 > n1 and n2 > n3:
    print('{} é o maior número'.format(n2))
    
else:
    print('{} é o maior número'.format(n3))
    
