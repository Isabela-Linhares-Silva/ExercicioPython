import random
a = str(input('Primeiro aluno:'))
b = str(input('Segundo aluno:'))
c = str(input('Terceiro aluno:'))
d = str(input('Quarto aluno:'))
lista = (a, b, c, d)
sorteio = random.choices(lista)
print('O aluno escolhido para apagar a lousa foi:{}'.format(sorteio))
