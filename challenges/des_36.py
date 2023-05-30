casa = float(input('Qual o valor do imóvel: R$ \n'))
salario = float(input('Quanto você recebe ao mês:R$ \n'))
tempo = float(input('Em quantos anos você quer pagar:\n'))

ano = tempo * 12
pres_mens = casa / ano
cond = salario * (30/100)

if pres_mens >= cond:
    print("Seu crédito foi negado!")
    
else: 
    print('Seu crédito foi aprovado!')
