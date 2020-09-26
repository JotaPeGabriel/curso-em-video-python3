"""Exercício Python 051:
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""
primeiro = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a Razão: '))
decimo = primeiro + (10 - 1) * primeiro
for c in range(primeiro, decimo + razão, razão):
    print(c, end='→ ')
print('ACABOU')
