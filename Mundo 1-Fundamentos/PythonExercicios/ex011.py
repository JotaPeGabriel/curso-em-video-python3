print('===== DESAFIO 011 =====')

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade necessaria
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²(dois metros quadrados).

print('Meça a parede e me diga em metros:')
larg = float(input('Qual a altura: '))
alt = float(input('Qual a largura: '))

area = larg * alt
tinta = area / 2

print(f'Voce ira precisar de {tinta}lt de tinta para pintar a area de {area}m²')
