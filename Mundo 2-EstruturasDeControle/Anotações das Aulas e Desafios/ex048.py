"""Exercício Python 048:
Faça um programa que calcule a soma entre todos os números que são
múltiplos de três e que se encontram no intervalo de 1 até 500."""
inpar = 0
resultado = 0
for c in range(3, 501, 2):
    if c % 3 == 0:
        inpar += 1
        resultado += c
print(f'O Valor da SOMA dos {inpar} numeros é de : {resultado}')
