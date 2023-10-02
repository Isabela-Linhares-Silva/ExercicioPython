from datetime import date
totmaior = 0
totmenor = 0
for c in range(1, 8):
    a = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    i = date.today().year - a
    if i >= 18:
        totmaior += 1
    elif i < 18:
        totmenor += 1
print('Tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))
