a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
maior = a
if c > b and c > a:
    maior = c
if b > a and b > c:
    maior = b
print('O maior valor é: {} '.format(maior))
menor = c
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
print('O menor valor é: {} '.format(menor))
