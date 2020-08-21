"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""
print('FINALIZANDO SEU CARRINHO DE COMPRAS')
preco = float(input('Preço: R$'))
print(f"""
Qual sera a forma de pagamento de Pagamento:
[1] À vista DINHEIRO - 10% desconto
[2] À vista DEBITO - 5% desconto
[3] Até 2x no CRÉDITO - Preço normal
[4] 3x no CRÉDITO - 20% de Juros
""")
opcao = int(input('Sua opção: '))
if opcao == 1:
    valor = preco - (preco * 10 / 100)
elif opcao == 2:
    valor = preco - (preco * 5 / 100)
elif opcao == 3:
    parcela = preco / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opcao == 4:
    valor = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = valor / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
else:
    valor = preco
    print('OPÇÃO INVALIDA')
print(f'Sua compra de R${preco:.2f} vai custar R${valor:.2f} no final.')
