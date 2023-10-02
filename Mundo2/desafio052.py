n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m''O número foi divido {} vezes'.format(tot))
if tot == 2:
    print('O número é PRIMO')
else: 
    print('O número NÃO É PRIMO')
