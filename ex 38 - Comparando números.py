n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
if n1 > n2:
    print('O primeito número digitado, {} é MAIOR do que {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo número digitado {}, é MAIOR do que {}'.format(n2,n1))
else:
    print('Não existe valor maior, os dois são iguais')