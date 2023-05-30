from random import randint

cont = 0
while True:
    n = randint(10,100)
    print(n)
    cont+=1
    if cont == 1000:
        break