"""Exercício Python 050:
Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."""
soma = 0
print('Vamos somar 6 numeros pares e interios')
for c in range(1, 7):
    num = int(input(f'digite um numero: '))
    if num % 2 == 0:
        soma += num
print(f' O valor da soma foi {soma}')
