nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Analizando seu nome, Espere um pouco...')
print(f'Em Caixa alta: {nome.upper()}')
print(f'Em Caixa baixa: {nome.lower()}')
print(f"Seu nome possui {len(nome) - nome.count(' ')} caracteres")
print(f'E seu primeiro nome tem {(len(dividido[0]))} caracteres')
