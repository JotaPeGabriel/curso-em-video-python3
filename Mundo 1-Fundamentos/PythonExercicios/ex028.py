from random import randint
from time import sleep
"""
print('Olá, vamos jogar!')
sorte = randint(0, 5)
num = int(input('Eu pensei em um numero, Adivinhe qual é: '))
if num == sorte:
    print('Uouu Parabens, Voce acertou de Primeira!')
else:
    print('Ops, errou...\n Ai vai um dica: o Numero é entre 0 e 5')
num2 = int(input('Tente de novo: '))
if num2 == sorte:
    print('Voce acertou!')
else:
    print(f'Não foi dessa vez :( \n o Numero certo era {sorte}')
#POS CORREÇÃO -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você consguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no numero {computador} e não no {jogador}!')
