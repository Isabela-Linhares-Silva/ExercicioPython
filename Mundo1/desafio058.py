from random import randint
comp = randint(0, 10)
tentativa = 0
print('''Sou o seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi ?''')
joga = int(input('Qual é o seu palpite? '))
while joga != comp:
    tentativa +=1
    if joga > comp:
        print('Menos... Tente mais uma vez.')
    if joga < comp:
        print('Mais... Tente mais uma vez.')
    joga = int(input('Qual é o seu palpite? '))
    if joga == comp:
        print('Acertou com {} tentativas. Parabéns!'.format(tentativa+1))
