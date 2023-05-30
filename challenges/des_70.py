print(27*'-')
print(10*' ','Loja')
print(27*'-')

soma= caros= 0
m_barato = float('inf')
n_barato=''

while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço:'))
    
    if valor < m_barato:
        m_barato = valor
        n_barato = produto
    
    soma+=valor
    
    if valor > 1000:
        caros +=1
    
    while True:
        op = str(input('Quer continuar: [S/N]')).upper().replace(' ', '')
        if op != 'S' or op != 'N':
            break        
    if op == 'N':
        break
    
print(f'O total da compra é de {soma}')
print(f'{caros} produtos custaram mais de R$1000.00')
print(f'O produto mais barato foi {n_barato} e custou {m_barato}')   