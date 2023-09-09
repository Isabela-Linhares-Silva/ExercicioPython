v = int(input('Qual é a velocidade atual do carro ? '))
m = (v-80) * 7
if v >= 81:
    print('Você foi multado por exceder o  limite permitido de 80km/h!')
    print('Você deve pagar uma multa de {:.2f}!'.format(m))
print('Tenha um bom dia! Diriga com segurança!')
