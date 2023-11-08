from random import randint
v = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR:')
print('=-' * 20)
while True:
    jog = int(input('Digite um valor: '))
    comp = randint(1, 10)
    total = jog + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR [P/I]: ')).upper().strip()
    print('-'*36)
    print(f'Você jogou {jog} e o computador jogou {comp}.Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    print('-'*36)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            print('*'*20)
            v += 1
        else:
            print('Você PERDEU!')
            print('*'*20)
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
print(f'GAME OVER... Você venceu {v} vezes.')