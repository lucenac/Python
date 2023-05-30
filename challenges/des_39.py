from datetime import date

atual = date.today().year
ano = int(input('Opa, qual ano você nasceu?\n'))
idade = atual - ano
if idade > 18:
    tempo = idade - 18
    print('Já passou {} ano(os) do periodo de se alistar!'.format(tempo))
    
elif idade < 18:
    tempo = 18 - idade
    print('Faltam {} ano(os) para você se alistar!'.format(tempo))
    
else:
    print('Está na hora de se alistar!')