print('===== DESAFIO 020 =====')
"""# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno = ('Ana', 'Vitoria', 'Julio', 'Bernardo')
print(f'A ordem para apresentação sera {random.sample(aluno,4)}"""
from random import shuffle

a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem para apresentação será: \n {lista}')