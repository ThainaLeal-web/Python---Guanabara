lista = []

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
       print('Valor adicionado com sucesso...')
       lista.append(n)
       resp = str(input('Deseja continuar? S/N ')).upper()
       if resp == 'N':
           break
    else:
        print('valor duplicado... Não adicionado!')
lista.sort()
print(lista)