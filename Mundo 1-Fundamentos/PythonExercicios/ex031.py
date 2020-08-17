km = float(input('Qual a distancia da sua viagem em Km: '))
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
    print('Sera uma longa viagem...')
print(f'Sua viagem vai custar R${preço:.2f}')
