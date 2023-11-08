Ii = Ss = V = 0
while True:
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if i >= 18:
        Ii += 1
    if s == 'M':
        Ss += 1
    if s == 'F' and i < 20:
        V += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar ? [S/N] ')).upper().strip()
        print('-'*20)
    if c == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {Ii}')
print(f'Ao todo temos {Ss} homens cadastrados;')
print(f'E temos {V} mulheres com menos de 20 anos.')