import math

co = float(input('Digite o cateto oposto:\n'))
ca = float(input('Digite o cateto adjacente\n'))

h = math.hypot(co, ca)

print('O valor da sua hipotenusa é {:.2f}'.format(h))
