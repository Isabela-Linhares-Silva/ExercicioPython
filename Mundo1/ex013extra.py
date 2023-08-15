v = float(input('Qual o valor do produto? R$'))
av = v - (v * 10/100)
p = v + (v * 8/100)
print('O produto comprado a vista é R${:.2f} e se for parcelado fica por R${:.2f}'.format(av,p))
