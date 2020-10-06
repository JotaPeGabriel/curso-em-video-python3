"""Exercício Python 055:
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""
maior = 0
menor = 99999999
for pess in range(1, 6):
    peso = float(input(f'Digite o {pess}º peso: '))
    if peso > maior:
        maior = peso
    else:
        menor = peso
print(f'O maior peso foi o {maior} e o menor peso foi o {menor}')
