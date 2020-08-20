"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
 e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

if idade <= 9:
    print(f'Com {idade} sua classificação é: MIRIM')
elif idade <= 14:
    print(f'Com {idade} sua classificação é: INFANTIL')
elif idade <= 19:
    print(f'Com {idade} sua classificação é: JUNIOR')
elif idade <= 25:
    print(f'Com {idade} sua classificação é: SÊNIOR')
else:
    print(f'Com {idade} sua classificação é: MASTER')
