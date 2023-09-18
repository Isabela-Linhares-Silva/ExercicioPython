v = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
O = input('Sua opção: ')
if O == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(v, bin(v)[2:]))
elif O == 2:
    print('{} convertido para OCTAL é igual a {}'.format(v, oct(v)[2:]))
else:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(v, hex(v)[2:]))
