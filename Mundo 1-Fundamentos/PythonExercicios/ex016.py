"""print('===== DESAFIO 016 =====')
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um numero: 6.127 / O número 6.127 tem a parte inteira 6
from math import trunc
num = float(input('Digite um número: '))
print(f"O número {num} tem a parte inteira {trunc(num)}")"""

num = float(input('Digite um valor: '))
print(f'o valo digitado foi {num} e a sua porção inteira é {int(num)}')
