p = float(input('Qual o seu peso ? '))
a = float(input('Qual a sua altura? '))
imc = p/(a**2)
print('O IMC dessa pessoa é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal! ')
elif 18.5 <= imc < 25:
    print('Você está no seu peso ideal!')
elif 25 <= imc < 30:
    print('Você está sobrepeso!')
elif 30 <= imc < 40:
    print('Você está na faixa de obesidade!')
elif 40 <= imc:
    print('Você está na faixa de obesidade mórbida!')