from random import randint
itens = ('pedra', 'papel', 'tesoura')
c = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
j = int(input('Qual a sua jogada? '))
print('=-'*12)
print('Computador jogou {}'.format(itens[c]))
print('Jogador jogou {}'.format(itens[j]))
print('=-'*12)
if c == 0:
    if j == 0:
        print('EMPATE!')
    if j == 1:
        print('JOGADOR GANHOU!')
    if j == 2:
        print('COMPUTADOR GANHOU!')
elif c == 1:
    if j == 0:
        print('COMPUTADOR GANHOU!')
    if j == 1:
        print('EMPATE!')
    if j == 2:
        print('JOGADOR GANHOU !')
elif c == 2:
    if j == 0:
        print('JOGADOR GANHOU !')
    if j == 1:
        print('COMPUTADOR GANHOU !')
    if j == 2:
        print('EMPATE !')
