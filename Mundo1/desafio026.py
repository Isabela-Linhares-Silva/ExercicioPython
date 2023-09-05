f = str(input('Digite uma frase: ')).strip().upper()
print('Esta frase possui', f.count('A'), 'letras A')
print('A primeira letra A apareceu na posição {}'.format(f.find('A')+1))
print('A última letra A apareceu na posição {}'.format(f.rfind('A') + 1))
