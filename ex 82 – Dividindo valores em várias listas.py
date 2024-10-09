lista = []
par = []
impar = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    resp = input('Deseja adicionar mais um número: [S/N] ').upper()[0]
    if resp == 'N':
        break
    while resp != 'S':
        print('[ERROR]')
        resp = input('Deseja adicionar mais um número: [S/N] ').upper()[0]
lista.sort()
impar.sort()
par.sort()
print(f'Os números digitados foram: {lista}')
print(f'Os números pares são: {par}')
print(f'Os números impares são: {impar}')
