num = int(input('Digite um número:\n'))
print('Escolha uma base de conversão:\n1-binário\n2-octal\n3-hexadecimal')
choice = int(input('Escolha uma opção: '))

if choice == 1:
    print('O número {} em binário é {}'.format(num, bin(num)[2:]))
    
elif choice == 2:
    print('O número {} em octal é {}'.format(num, oct(num)[2:]))
    
elif choice == 3:
    print('O número {} em hexadecimal é {}'.format(num, hex(num)[2:]))
    
else:
    print('você escolheu uma opção não existente')
        