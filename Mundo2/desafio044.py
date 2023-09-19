print('=======LOJA MANEIRA=======')
v = float(input('Qual o valor da compra? '))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
o = input('Qual é a opção? ')
if o == 1:
    d = v - v*10/100
elif o == 2:
    d = v - v*5/100
elif o == 3:
    d = v
    d1 = v/2
    print('Sua compra será parcelada em 2x de R${}'.format(d1))
elif o == 4:
    p = int(input('Quantas parcelas? '))
    d = v*20/100 + v
    g = d / p
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(p, g))
else:
    d = v
    print('Opção \033[31minváliva\033[m! Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(v, d))
