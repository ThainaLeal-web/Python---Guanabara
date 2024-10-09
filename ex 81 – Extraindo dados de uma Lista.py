lista = []

while True:
    n = int(input('Digite um valor: '))

    lista.append(n)
    resp = input('Deseja continuar? [S/N] ').upper()[0]
    if resp == 'N':
        break
    while resp != 'S':
        print('resposta incorreta')
        resp = input('Deseja continuar? [S/N] ').upper()[0]

print(f'No total foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'De forma descrescente {lista}')
if 5 in lista:
    print('o valor 5 está na lista!')
else:
    print('O valor 5 NÃO foi encontrado')