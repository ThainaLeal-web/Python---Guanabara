def leiaInt(n):
    while not n.isnumeric():
        print('NÃO é um número!')
        n = leiaInt(input('Digite um número: '))
    if n.isnumeric():
        return n


#Programa Principal
n = leiaInt(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}')