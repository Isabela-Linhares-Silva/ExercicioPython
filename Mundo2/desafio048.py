soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
print('A soma de todos os valores solicitado é {}.'.format(soma))
