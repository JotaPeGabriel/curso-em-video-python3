"""Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
 1 para binário,
 2 para octal e
 3 para hexadecimal.
 """
numero = int(input('Digite um numero inteiro: '))

conversao = int(input('Escolha qual será a base de conversão:\n 1 para binário\n 2 para octal\n 3 para hexadecimal\n'))

if conversao == 1:
    print(f'O valor {numero} em binario é {bin(numero)}')
elif conversao == 2:
    print(f'O valor {numero} em binario é {oct(numero)}')
elif conversao == 3:
    print(f'O valor {numero} em binario é {hex(numero)}')
else:
    print("Voce digitou algo errado")