#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: Á média de idade do grupo; Qual o nome do homem mais velho; Quantas mulheres têm menos de 20 anos.

cont_fem = 0 
idade_masc = 0
media_idade = 0
homem_velho = ''

for c in range(0, 4):
    nome = str(input('Qual o nome da pessoa {}? '.format(c+1)))
    idade = int(input('Quantos anos a pessoa {} tem? '.format(c+1)))
    sexo = str(input('Qual o sexo dela? [M/F]')).replace(' ', '').upper()
    
    media_idade+=idade
    
    if sexo == 'F' and idade < 20:
        cont_fem+=1
        
    if idade_masc < idade and sexo == 'M':
        idade_masc = idade
        homem_velho = nome

media_idade = media_idade / 4        

print('A média da idade do grupo é de {}; O homem mais velho tem {} e se chama {} e tem {} mulheres com menos de 20 anos no grupo...'.format(media_idade, idade_masc, homem_velho, cont_fem))