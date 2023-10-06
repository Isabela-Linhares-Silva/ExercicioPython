somaidade = 0
mediaidade = 0
maioridade = 0
maisvelho = ''
totmaior = 0
for c in range(1, 5):
    print('----{}ª PESSOA----'.format(c))
    n = str(input('Nome:')).strip()
    i = int(input('Idade:'))
    s = str(input('Sexo [M/F]:')).strip()
    somaidade += i
    if c == 1 and s in 'Mm':
        maioridade = i
        maisvelho = n
    if s in 'Mm' and i > maioridade:
        maioridade = i
        maisvelho = n
    if s in 'Ff' and i < 20:
        totmaior += 1
mediaidade = somaidade/4
print('A média das idades é {} anos.'.format(mediaidade))
print('O mais velho se chama {} e tem {} anos.'.format(maisvelho, maioridade))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmaior))

