print('Triangulo')

r1 = float(input('Digite o tamanho do primeiro segmento: '))
r2 = float(input('Digite o temanho do segundo segmento: '))
r3 = float(input('Digite o tamanho do terceiro segmento: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('Você pode formar um triângulo')
    if r1 == r2 == r3:
        print('Você pode formar um triângulo equilátero')
        
    elif r1 == r2 or r1 ==r3 or r2==r3:
        print("Você pode formar um triângulo isósceles")
    
    else:
        print('Você pode formar um triângulo escaleno')
else:
    print('Você não pode formar um triângulo')
    