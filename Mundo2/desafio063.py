print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)
t = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
c = 3
print('{}_{}'.format(t1, t2),end='_')
while c <= t:
    t3 = t1 + t2
    print(t3, end='_')
    t1 = t2
    t2 = t3
    c += 1
print('Fim!')
