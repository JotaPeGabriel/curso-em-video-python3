nome = input('Digite seu nome: ')
n1 = int(input('Digite um valor: '))
n2 = int(input('outro numero: '))

s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'{nome:=^50}')
print(f'A soma é {s},\n a subtração é {sb},\n o produto é {m} e a divisão é {d:.3f}', end=' | ')
print(f'Divisão inteira {di} e potencia {e}')
