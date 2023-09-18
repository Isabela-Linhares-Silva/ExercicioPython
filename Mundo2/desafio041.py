from datetime import date
a = int(input('Ano de nascimento: '))
e = date.today().year
i = e - a
print('O(A) atleta tem {} anos.'.format(i))
if i <= 9:
    print('Categoria: MIRIM')
elif 10 <= i <= 14:
    print('Categoria: INFANTIL')
elif 15 <= i <= 19:
    print('Categoria: JÚNIOR')
elif 20 <= i <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')