soma = 0
for c in range(1,501):
    if c  %2 != 0:
        if c %3 == 0:
            soma += c
        
print(soma)