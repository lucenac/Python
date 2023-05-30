#formula: (0 °C × 9/5) + 32 = 32 °F
celsius = float(input('Digite o valor em Celcius:\n'))

fahrenheit = (celsius * 9/5) + 32 

print('{} C° é igual à {:.1f} F°!'.format(celsius, fahrenheit))