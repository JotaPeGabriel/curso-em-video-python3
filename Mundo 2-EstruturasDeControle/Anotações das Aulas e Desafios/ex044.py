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
    valor = preco - (preco * 0.10)
elif opcao == 2:
    valor = preco - (preco * 0.05)
elif opcao == 3:
    parcela = preco / 2
    print(f'Sera parcelado em 2x de R${parcela:.2f} (SEM JUROS)')
elif opcao == 4:
    valor = preco + (preco * 0.20)
    numparcela = int(input('Quantas parcelas: '))
    parcela = valor / numparcela
    print(f'Sera parcelado em {numparcela}x de R${parcela:.2f} (COM JUROS)')
else:
    valor = preco
    print('OPÇÃO INVALIDA')
print(f'Valor a pagar R${valor:.2f} dos R${preco:.2f} iniciais')
