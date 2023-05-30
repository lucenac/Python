larg = float(input('Qual a largura da sua parede?\n'))
alt = float(input('Qual a altura da sua parede?\n'))

area = larg * alt
tinta = area / 2

print('Será necessário {:.2f} litros de tinta!'.format(tinta))