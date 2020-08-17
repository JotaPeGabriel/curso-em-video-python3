print('===== DESAFIO 019 =====')
"""
# Um professor quer sortear um dos seu quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
aluno = ('Ana', 'Vitoria', 'Julio', 'Bernardo')
print(f'o Aluno sorteado foi: {choice(aluno)}')"""
from random import choice
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print(f'o Aluno sorteado foi: {escolhido}')
