"""
carro = int(input('Qual foi a velocidade do carro: '))
if carro >= 80:
    multa = (carro - 80)*7
    print(f'Voce foi multado em R${multa}')
else:
    print('Sem problemas por aqui, pode seguir')
#POS CORREÇÃO -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar um multa de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com Segurança!')
