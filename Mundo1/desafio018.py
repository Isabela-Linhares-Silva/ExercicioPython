import math
a = (float(input('Digite um ângulo:')))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O valor do seno é {:.2f}, o do cosseno é {:.2f} e a tangente é {:.2f}'.format(s,c,t))