n = int(input('Digite um número: '))
c=n
f=1

for i in range(1,n+1):
    print(c,end='')
    print(' x ' if c >1 else ' = ', end='')
    f*=i
    c-=1
print(f)