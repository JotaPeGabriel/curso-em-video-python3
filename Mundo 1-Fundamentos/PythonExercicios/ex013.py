print('===== DESAFIO 013 =====')

# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.

# sal = float(input('Qual seu salario atual? R$'))
# aum = sal * 0.15
# nsal = sal + aum
# print(f"Seu novo salario é de R${nsal:.2f} e o aumento foi de R${aum:.2f}")
# print('PÓS CORREÇÃO----------------------------------')

salário = float(input('Qual é o salario do Funcionario? R$'))
novo = salário + (salário * 15 / 100 )
print(f'Um funcionário que ganhava R${salário:.2f}, com 15% de aumento, passa a receber R${novo:.2f}')