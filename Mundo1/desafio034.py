s = float(input('Qual é o salário do funcionário? R$ '))
if s > 1250.00:
    print('Quem ganhava {:.2f}, passa a ganhar {:.2f}.'.format(s,(s*0.1)+s))
else:
    print('Quem ganhava {:.2f}, passa a ganhar {:.2f}.'.format(s, (s*0.15)+s))
