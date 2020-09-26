"""Exercício Python 051:
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""
termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a Razão: '))
limite = termo + (10 - 1) * razao
for c in range(termo, limite + termo, razao):
    print(c, end='- ')
print('FIM')
