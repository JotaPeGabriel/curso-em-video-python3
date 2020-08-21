"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""
peso = float(input('Digite o peso:(Kg) '))
altura = float(input('Digite a altura:(m) '))
imc = peso / (altura * altura)
print(f'O seu IMC esta em {imc:.2f}')
if imc < 18.5:
    print('CUIDADO! Você está ABAIXO DO PESO ideal.')
elif 18.5 <= imc <= 25:
    print('PARABENS! Você está no PESO IDEAL ')
elif 25 < imc < 30:
    print('Melhor ficar ALERTA! Você esta com SOBREPESO')
elif 30 <= imc < 40:
    print('CUIDADO! Você está com OBESIDADE')
else:
    print('URGENTE! Você esta com OBESIDADE MORBIDA')