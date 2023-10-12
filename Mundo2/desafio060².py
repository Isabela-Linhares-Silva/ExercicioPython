from math import factorial
f = int(input('Digite um número para saber o seu fatorial:'))
s= factorial(f)
print('{}! ='.format(f),end=' ')
for f in range(f, 0, -1):
    print(f, end='')
    print(' x 'if f > 1 else ' = ', end='')
print(s)
