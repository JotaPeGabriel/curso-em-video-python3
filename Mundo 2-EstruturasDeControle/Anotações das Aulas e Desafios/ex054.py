"""Exercício Python 054:
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""
from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Digite o {c}º Ano de nascimento : '))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'O numero de MAIORES de idade foi de {maior} e de MENORES de idade foi de {menor} ')
