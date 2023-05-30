cont_idade= cont_sexo= cont_homem= cont_mulher =0

while True:
    print('Cadastre uma pessoa')
    print('-'*30)
    idade = int(input('Idade: '))
    if idade >= 18:
        cont_idade+=1
    sexo = str(input('Sexo: [M/F] ')).upper().replace(' ', '')
    while sexo != 'M' and sexo!= 'F':
        sexo = str(input('Sexo: [M/F] ')).upper().replace(' ', '')
    if sexo == 'M':
        cont_homem+=1
    if sexo == 'F' and idade <= 20:
        cont_mulher+=1
    print('-'*30)
    op = str(input('Quer continuar? [S/N] ')).upper().replace(' ', '')
    while op != 'S' and op != 'N':
        op = str(input('Quer continuar? [S/N] ')).upper().replace(' ', '')
    if op == 'N':
        break
    print('-'*30)
print('Fim do programa')
print(f'Total de pessoas com mais de 18 anos: {cont_idade}')
print(f'Total de homens cadastraddos:{cont_homem}')
print(f'Total de mulheres menores de 20 anos: {cont_mulher}')