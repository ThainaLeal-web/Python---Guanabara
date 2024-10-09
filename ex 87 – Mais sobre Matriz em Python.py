matriz = [[],[],[]]
spar = somat = maiorv = 0

for l in range(0,3):
    for c in range(0,3):
        n = int(input(f'Digite um valor [{l}, {c}]: '))
        matriz[c].append(n)
        if n % 2 == 0:
            spar += n
        if c == 2:
            somat += n
        if l == 1 and maiorv < n:
            maiorv = n
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[c][l]:^5}', end=' ')
    print( )
print('-='*30)

#A soma de todos os valores pares digitados
print(f'A soma de todos os números pares foram: {spar}')
#A soma dos valores da terceira coluna
print(f'A soma dos valores da terceira coluna: {somat}')
#O maior valor da segunda linha
print(f'O maior valor da segunda linha é: {maiorv}')



