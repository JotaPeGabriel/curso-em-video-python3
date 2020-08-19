""" Condições Aninhadas
if = se
elif = SeNão Se (só pode ser usado em seguida de um if)
else = SeNão (Não tem a obrigração de existir caso seja utilizado o IF ou ELIF)
"""

nome = str(input('Qual é seu nome? ')).strip()
if nome == 'Jose':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')
