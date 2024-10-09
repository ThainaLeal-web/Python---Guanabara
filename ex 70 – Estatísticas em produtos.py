print('---'*10)
print('    LOJA SUPER BARATÃO')
print('---'*10)

tot = 0
valm = 0
vmenor = 10000000000000000000000000000000
nmenor = ' '

while True:
    prod = input('Nome do produto: ')
    val = float(input('Preço: R$'))
    tot += val
    if val > 1000:
        valm += 1
    if val < vmenor:
        nmenor = prod
        vmenor = val
    resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':
        break

print(f'O total da compra é R${tot}')
print(f'No total, {valm} produtos, custaram mais de R$1000')
print(f'O produto mais barato foi {nmenor}')
