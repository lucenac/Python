t = int(input('Quantos termos você quer que apareça? '))
t1 = 0
t2 = 1
print('{} → {} → '.format(t1,t2),end='')
cont = 1
while t > cont:
    cont += 1
    t3 = t1 + t2
    t1=t2
    t2=t3
    print('{} → '.format(t3),end='')
    
print('Fim')