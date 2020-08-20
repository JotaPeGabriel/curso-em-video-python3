"""Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
 se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print(f'Se voce nasceu em {ano} deve ter {idade} agora')
if idade < 18:
    print(f'Ainda FALTA(M) {18 - idade} ano(s) para se alistar ')
    print(f'Voce deve se alistar em {ano + 18}')
elif idade > 18:
    print(f'Seu periodo de alistamento já PASSOU a {idade - 18} ano(s)')
    print(f'Voce deveria se alistar em {ano + 18}')
elif idade == 18:
    print('Esta no ano de se Alistar')

