itens = ['lápis', 1.95,
         'Borracha', 1.80,
         'Caderno', 60,
         'Estojo', 12,
         'transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 100,
         'Canetas', 1.98,
         'Livro', 34.90]

print('-'*37)
print(f'{"Listagem de preços" :^37}')
print('-'*37)

for pos in range (0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}', end ='')
    else:
        print(f'R${itens[pos]:>6.2f}')
print('-'*37)