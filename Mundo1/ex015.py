d = int(input('Quantos dias alugados?'))
k = float(input('Quantos km rodados ?'))
t = (60 * d) + (0.15 * k)
print('O total a pagar é: R${}'.format(t))