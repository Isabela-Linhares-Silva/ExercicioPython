from math import factorial
f = int(input('Digite um número para saber o seu fatorial: '))
p = factorial(f)
print('{}! = '.format(f),end='')
while f > 0:
    print('{} '.format(f), end='')
    print('x ' if f > 1 else '= ', end='')
    f -= 1


print('{}'.format(p))
