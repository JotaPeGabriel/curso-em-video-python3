"""Exercício Python 049:
Refaça o DESAFIO 009, mostrando a tabuada de um número que o
usuário escolher, só que agora utilizando um laço for."""
x = int(input('Digite um numero para ser Multiplicado : '))
print('-' * 12)
print('TABUADA')
for c in range(1, 11):
    print(f'{x} X {c:2} = {x * c}')
print('-' * 12)

