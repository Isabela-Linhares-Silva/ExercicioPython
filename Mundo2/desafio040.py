n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
m = (n1 + n2)/2
print('Com as notas {} e {}, a média do aluno é {:.2f}.'.format(n1, n2, m))
if m < 5.0:
    print('O aluno está \033[31mREPROVADO \033[m!')
elif 5.0 <= m <= 6.9:
    print('O aluno está de \033[33mRECUPERAÇÃO \033[m!')
else:
    print('O aluno foi \033[32mAPROVADO \033[m!')