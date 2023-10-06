s = input('Informe o seu sexo: [M/F] ').upper().strip()
while s != 'F' and s != 'M':
       s = input('Dados inválidas! Informe o seu sexo: ').strip().upper()
if s == 'F':
       print('Sexo F registrado com sucesso!')
if s == 'M':
       print('Sexo M registrado com sucesso!')
print('Fim')
