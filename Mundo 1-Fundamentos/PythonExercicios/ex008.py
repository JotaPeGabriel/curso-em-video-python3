print('===== DESAFIO 008 =====')
metros = float(input('Uma distância em Metros:  '))

print(f'Esse é seu valor em Centimetros {metros * 100}\n Em milimitros {metros * 1000}')

print('PÓS CORREÇÃO----------------------------------')

mm = metros * 1000
cm = metros * 100
dm = metros * 10
da = metros / 10
hm = metros / 100
km = metros / 1000

print(f'As demais proporções de {metros}m são:\n {mm}mm \n {cm}cm \n {dm}dm \n {da}dam \n {hm}hm \n {km}km')
