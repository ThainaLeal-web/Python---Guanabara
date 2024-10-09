import time

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

op = 0

while op != 5:
    print('-=-'*20)
    print('[1] Somar \n[2] multiplicar\n[3] Maior\n[4] Novos números \n[5] Sair do programa')
    op = int(input('Qual a sua opção? '))

    if op == 1:
        print('A soma entre {} e {} é {}'.format(n1,n2,(n1+n2)))
    elif op == 2:
        print('{} * {} = {}'.format(n1,n2,(n1*n2)))
    elif op == 3:
        if n1 > n2:
            print('O valor {} é maior do que {}!'.format(n1,n2))
        elif n2 > n1:
            print('O valor {} é maior do que {}!'.format(n2, n1))
        else:
            print('Os valores digitados, são iguais!')

    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
        time.sleep(1)

print('Fim do programa! Volte sempre!')
