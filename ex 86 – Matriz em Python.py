lista = [[], [], []]

for l in range(0,3):
    for c in range(0,3):
        n = int(input(f'Digite um número: [{l}] [{c}] '))
        lista[c].append(n)
for l in range(0,3):
    for c in range(0,3):
        print(f'{lista[l][c]:^5}', end=' ')
    print( )