print('Calculadora Matemática')

while True:
    #entrada inicial
    num1= float(input('Digite um valor:'))
    num2= float(input('Digite outro valor:'))

    #menu
    print('''Escolha uma opção:
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa''')
    menu = int(input('Escolha uma opção: '))
    while menu < 1 or menu > 5:
        menu = int(input('Você escolheu uma opção não existente, escolha uma opção: '))
        
    if menu == 1:
            op = num1 + num2
            print('A soma de {} e {} é igual à {}'.format(num1,num2,op))

    #Multiplicar
    elif menu == 2:
            op = num1 * num2
            print('O produto de {} e {} é igual à {}'.format(num1,num2,op))
            
    #Maior
    elif menu == 3:
        if num1 > num2:
                op = num1
                print('{} é maior que {}'.format(op,num2))
        elif num1 < num2:
                op = num2
                print('{} é maior que {}'.format(op,num1))
        else:
                print('Os números são iguais')

    #Sair do programa
    elif menu == 5:
        print('Fim do programa!')
        break
    print('-=-'*10)
    #Novos números 
    while menu == 4:
        num1= float(input('Digite um valor:'))
        num2= float(input('Digite outro valor:'))
        menu = int(input('Escolha uma opção: '))
        while menu < 1 or menu > 5:
            menu = int(input('Você escolheu uma opção não existente, escolha uma opção: '))
        #Soma
        if menu == 1:
            op = num1 + num2
            print('A soma de {} e {} é igual à {}'.format(num1,num2,op))

        #Multiplicar
        elif menu == 2:
            op = num1 * num2
            print('O produto de {} e {} é igual à {}'.format(num1,num2,op))
            
        #Maior
        elif menu == 3:
            if num1 > num2:
                op = num1
                print('{} é maior que {}.format(op,num2)')
            elif num1 < num2:
                op = num2
                print('{} é maior que {}'.format(op,num1))
            else:
                print('Os números são iguais')

        #Sair do programa
        elif menu == 5:
            print('Fim do programa!')
            break
        print('-=-'*10)