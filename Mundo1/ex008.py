n = float(input('Digite um valor em metros:'))
k = n / 1000
h = n / 100
da =n / 10
dm = n * 10
c = n * 100
m = n * 1000
print('A medida de {}m corresponde a: \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm '.format(n,k,h,da,dm,c,m))