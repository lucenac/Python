n = int(input('Digite um número: '))
c = n
f=1

print('Caluculando {}! = '.format(c), end="")

while c > 0:
    print(c, end="")
    print(' x ' if c > 1 else ' = ', end='')
    f*=c
    c-=1
print(f)

