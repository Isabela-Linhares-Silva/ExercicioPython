v = float(input('Qual é o valor da casa ? R$'))
s = float(input('Informe o seu salário: R$'))
a = int(input('Em quantos anos você quer pagar ?'))
m = a * 12
p = v / m
if p <= s*30/100:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de {:.2f}.'.format(v, a, p))
    print('Empréstimo\033[34m CONCEDIDO\033[m!')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de {:.2f}'.format(v, a, p))
    print('Empréstimo\033[31m NEGADO\033[m!')