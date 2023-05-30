real = float(input('Quanto de dinheiro em real você tem?\n'))
conv = real / 3.27
print('Com R${}, você pode comprar U${:.2f}'.format(real, conv))