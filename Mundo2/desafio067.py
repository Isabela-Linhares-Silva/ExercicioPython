'''n = c = 0
n = int(input('Quer ver a tabuada de qual valor ? '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
    if n == '-n':
        break
print('Fim')'''
while True:
    n = int(input('Quer ver a tabuada de qual valor ? '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('Programa tabuada encerrado! Volte sempre!')