nome = str(input('Digite seu nome:')).strip()

separa = nome.split()

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} caractéres'.format(len(nome)-nome.count(" ")))
print('Seu primeiro nome é {} e tem {} carectéres'.format((separa[0]), len(separa[0])))