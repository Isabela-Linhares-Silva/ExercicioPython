print('-'*30)
print('       LOJA VARIÁVEIS')
print('-'*30)
soma = V = menor = cont = 0
barato = ''
while True:
    n = str(input('Nome do produto: '))
    v = int(input('Preço do produto: R$ '))
    c = ' '
    cont += 1
    soma += v
    if v >= 1000:
        V += 1
    if cont == 1:
        menor = v
        barato = n
    else:
        if v < menor:
            menor = v
    while c not in 'SN':
        c = str(input('Quer continuar ? [S/N] ')).upper().strip()
        print('~'*20)
    if c == 'N':
        break
print('-'*10, 'FIM DO PROGRAMA', '-'*10)
print(f'O total da compra foi de {soma}')
print(f'Temos {V} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
