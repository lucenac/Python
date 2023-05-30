nota1 = float(input('Digite sua nota da primeira prova:\n'))
nota2 = float(input('Digite sua nota da segunda prova:\n'))

nota_f = (nota1 + nota2) / 2

if nota_f >= 7:
    print('Aprovado!')
    
elif 5.0 <= nota_f <= 6.9:
    print('Recuperação!')
    
else:
    print('Reprovado!')