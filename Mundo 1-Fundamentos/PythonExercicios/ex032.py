from datetime import date
"""
ano = int(input('Digite um ano: '))
if ano % 4 != 0:
    ano % 400 != 0
    print(f'O ano de {ano} NÃO É bissextu')
else:
    print(f'O ano de {ano} É bissextu')
#POS CORREÇÃO -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')
