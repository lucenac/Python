#num = int(input())
#n = str(num)

#print(n[0])
#print(n[1])
#print(n[2])
#print(n[3])

num = int(input('Digite um número:'))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('O seu número é {}'.format(num))
print('A sua unidade é {}'.format(u))
print('A sua denzena é {}'.format(d))
print('A sua centena é {}'.format(c))
print('O seu milhar é {}'.format(m))