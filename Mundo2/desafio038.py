a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
if a > b:
    print('O \033[36m primeiro\033[m valor é maior.')
elif b > a:
    print('O \033[32msegundo\033[m valor é maior.')
elif a == b:
    print('Os dois valores são iguais.')