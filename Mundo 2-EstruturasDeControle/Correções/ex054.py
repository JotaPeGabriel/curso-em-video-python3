"""Exercício Python 054:
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""
from datetime import date
atual = date.today()
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    ano = int(input(f'Em que ano a {pess}º pessoa nasceu? '))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade.')
print(f'e também tivemos {totmaior} pessoas menores de idade.')
