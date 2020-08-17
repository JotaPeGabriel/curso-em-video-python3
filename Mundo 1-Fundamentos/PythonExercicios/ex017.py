print('===== DESAFIO 017 =====')
"""# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um trinagulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
from math import hypot
oposto = float(input("Digite o cateto oposto : "))
adj = float(input("DIgite o cateto adjacente : "))
print(f'O valor da hipotenusa ser {hypot(oposto,adj):.2f}')"""
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(ca, co)
print(f'A hipotenusa vai medir {hi:.2f}')
