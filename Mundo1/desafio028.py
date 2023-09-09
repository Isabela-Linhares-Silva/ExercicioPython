from random import randint
comp = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jog = int(input('Em que número eu pensei ?'))
if jog == comp:
    print('Você acertou! Parabéns!')
else:
    print('Ganheii! O número escolhido foi {}'.format(comp))
