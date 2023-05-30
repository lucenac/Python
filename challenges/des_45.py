import random
from time import sleep

#informations collect
itens = ['Pedra', 'Papel', 'Tesoura']
cpu_jkp = random.randint(0,2)


print('Vamos jogar Jonkepô! Você escolhera um valor que seja referente a sua jogada!')
p_jkp = int(input('''Escolha um desses!
    0-Pedra
    1-Papel
    2-Tesoura
Digite um valor: '''))

#Loading results
sleep(1)
print('JOKENPÔ')
sleep(1)

print('-='*11)
print('Computador jogou {}'.format(itens[cpu_jkp]))
print('Jogador jogou {}'.format(itens[p_jkp]))
print('-='*11)

#conditions

if cpu_jkp == 0:
   
    if p_jkp == 0:
        print('Empate!')
    elif p_jkp == 1:
        print('Jogador vence!')
    elif p_jkp == 2:
        print('CPU vence!')
    else: print('Jogada inválida')    


elif cpu_jkp == 1:
  
    if p_jkp == 0:
         print('CPU vence!')       
    elif p_jkp == 1:
        print('Empate!')
    elif p_jkp == 2:
        print('Jogador vence!')       
    else: print('Jogada inválida')


elif cpu_jkp == 2: 
    if p_jkp == 0:
        print('Jogador vence!')        
    elif p_jkp == 1:
        print('CPU vence!')
    elif p_jkp == 2:
        print('Empate!')        
    else: print('Jogada inválida')