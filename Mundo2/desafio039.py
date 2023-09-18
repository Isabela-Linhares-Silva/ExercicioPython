from datetime import date
O = int(input('''Qual é o seu sexo?'
[1]Feminino
[2]Masculino
Sua opção: '''))
if O == 1:
    print('Você não precisa se alistar !')
elif O == 2:
    d = date.today().year
    n = int(input('Em que ano você nasceu ? '))
    i = d - n
    print('Você nasceu em {}, tem {} anos em {}.'.format(n, i, d))
    if i > 18:
        print('Você já deveria ter se alistado há {} ano(s).'.format(i - 18))
        print('Seu alistamento foi em {}.'.format(n + 18))
    elif i < 18:
        print('Ainda falta(m) {} anos para o alistamento.'.format(18 - i))
        print('Seu alistamento será em {}.'.format(n + 18))
    else:
        print('Você tem que se alistar imediatamente!!!')
