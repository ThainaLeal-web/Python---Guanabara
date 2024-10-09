
número = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')), int(input('Digite um último valor: ')))
print(número)
print(f'O total de vezes que o número 9 aparece é {número.count(9)}')
if 3 in número:
    print(f'O primeiro valor 3, é encontrado na posição {número.index(3)+1}')
else:
    print('Não foi encontrado o número 3')
print('Os números pares digitados são: ', end=' ')
for n in número:
    if n % 2 == 0:
        print(n, end=' ')