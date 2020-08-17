print('===== DESAFIO 012 =====')

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# prod = float(input('Qual o Valor do produto? R$ '))
# desc = prod * 0.05
# preco = prod - desc
# print(f'O novo valor é de R${preco:.2f} e o valor de desconto foi R${desc:.2f}')
# print('PÓS CORREÇÃO----------------------------------')

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print(f'O produto que custava R${preço}, na promoção com desconto de 5% vai custar R${novo}')

