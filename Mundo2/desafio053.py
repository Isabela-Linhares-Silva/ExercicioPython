f = str(input('Digite uma frase: ')).upper().strip()
palavra = f.split()
junto = ''.join(palavra)
inverso = ''
for c in range(len(junto)-1, -1, -1):
    inverso += junto[c]
print('O inverso de {} é {}.'.format(junto,inverso))
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
