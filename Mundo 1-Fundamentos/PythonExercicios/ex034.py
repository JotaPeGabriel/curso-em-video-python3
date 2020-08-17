salario = float(input('Qual o seu Salário? R$'))
if salario > 1250.00:
    aumento = (salario * 0.10) + salario
else:
    aumento = (salario * 0.15) + salario
print(f'Seu novo salário sera: R${aumento:.2f}')
