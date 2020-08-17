print('===== DESAFIO 010 =====')

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteria e  mostre quantos Dólares ela pode comprar.

r = float(input("Quanto dinheiro voce tem na carteira? R$"))
dr = r / 5.12
eu = r / 5.80

print(f'Voce teria {dr:.2f} em Dolares em 05/06/2020 \n'
      f'  Ou teria {eu:.2f} em Euros em 05/06/2020 ')
