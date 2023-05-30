nome = str(input('Qual o seu nome? ')).lower().strip()
print('A letra A aparece {} vez(ezes) na frase'.format(nome.count('a')))
print('A primeira letra A apareceu na posição {}'.format(nome.find('a')))
print('A última letra A apareceu na posição {}'.format(nome.rfind('a')))