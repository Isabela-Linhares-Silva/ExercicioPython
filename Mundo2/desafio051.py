print('=-'*18)
print('       10 TERMOS DE UMA PA')
print('=-'*18)
a1 = int(input('Primeiro termo:'))
r = int(input('Razão:'))
print(a1, end=' ')
for pa in range(1, 10):
    a = a1+r
    print(a*pa, end=' ')

