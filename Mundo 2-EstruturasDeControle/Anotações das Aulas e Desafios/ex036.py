"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""
from time import sleep

print('Bem vindo(a) a analise de credito, Credita')
valorcasa = float(input('valor da casa: R$'))
salario = float(input('QuaL seu salario: R$'))
tempo = int(input('Em quantos ANOS pretente pagar: '))
print('ANALIZANDO...')
sleep(3)
parcelas = valorcasa / (tempo * 12)
print(f'O valor das parcelas sera de R${parcelas:.2f} mensais')
if parcelas > (salario * 30 / 100):
    print(f'Infelizmente seu empréstimo foi NEGADO')
else:
    print(f'Seu empréstimo foi APROVADO')
