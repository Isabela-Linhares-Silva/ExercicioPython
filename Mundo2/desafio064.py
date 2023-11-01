n = 0
s = 0
tot = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    s += n
    tot += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma deles foi {}'.format(tot, s))
