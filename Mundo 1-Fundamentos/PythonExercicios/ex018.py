print('===== DESAFIO 018 =====')
"""# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math
angulo = int(input("Digite um angulo: "))
print(f"O valor do Seno {math.sin(angulo)}\n Conseno {math.cos(angulo)}\n Tangente {math.tan(angulo)}")"""
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o Cosseno de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o Tangente de {tangente:.2f}')
