from time import sleep
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor:'))
c = ''
while c != 5:
    c = int(input('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números 
    [ 5 ] sair do programa
>>>>> Qual é a sua opção? '''))
    if c == 1:
        print('A soma entre {} + {} é {}'.format(a, b, a+b))
    elif c == 2:
        print('A multiplicação entre {} x {} é {}'.format(a, b, a*b))
    elif c == 3:
         if a > b:
             print('Entre {} e {} o maior valor é {}'.format(a, b, a))
         else:
             print('Entre {} e {} o mair valor é {}'.format(a, b, b))
    elif c == 4:
        a = int(input('Digite o primeiro valor:'))
        b = int(input('Digite o segundo valor:'))
    elif c == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente!')
    print('=-='*10)
print('Fim do programa! Volte sempre!')