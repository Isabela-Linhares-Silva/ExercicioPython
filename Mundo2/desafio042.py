r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2< r3 + r1 and r3 < r2+r1:
    print('Os segmentos podem formar triângulos!')
    if r1 == r2 == r3:
        print('Um triângulo equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Um triângulo isóceles.')
    else:
        print('Um triângulo escaleno.')
else:
    print('Os segmentos não podem formam um triângulo.')
