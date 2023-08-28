'''import math
a = int(input('Digite o valor do cateto adjacente:'))
o = int(input('Digite o valor do cateto oposto:'))
h = (a**2 + o**2)**(1/2)
print('Sendo o cateto adjacente de um triangulo retângulo igual a {} e o cateto oposto {} o valor da hipotenusa é {}'.format(a, o,h))'''

from math import hypot
a = float(input('Digite o valor do cateto adjacente:'))
o = float(input('Digite o valor do cateto oposto:'))
h = hypot(a, o)
print('A hipotenusa vai medir:{:.2f}'.format(h))