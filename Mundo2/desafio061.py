print('10 PRIMEIROS TERMOS DE UMA PA')
print('-='*15)
a = int(input('Primeiro termo: '))
b = int(input('Razão da PA: '))
termo = a
c = 1
while c < 11:
    print('{}'.format(termo), end=' ')
    termo += b
    c += 1
print('Fim')
