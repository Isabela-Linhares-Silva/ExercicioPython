print('GERADOR DE PA:')
print('=-='*8)
a = int(input('Primeiro termo: '))
r = int(input('Razão: '))
mais = 11
termo = a
c = 1
tot = 0
while mais != 0:
    tot += mais
    while c < tot:
        print('{}'.format(termo), end=' ')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais ? '))
print('No final você viu {} termos'.format(tot-1))
print('Fim!!')
