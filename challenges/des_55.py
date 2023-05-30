num_pes = 5
pesos = []
for c in range(num_pes):
    peso = float(input('Qual o peso da pessoa {}?'.format(c+1)))
    pesos.append(peso)

peso_max = max(pesos)
peso_min = min(pesos)

print('O maior peso é de {} kg, já o menor é de {} kg.'.format(peso_max,peso_min))
