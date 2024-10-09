div = 0
n = int(input('Digite um número: '))
for c in range(1, n +1, 1):
    if n % c == 0:
        print('\033[0;32m', end=' ')
        div = div + 1
    else:
        print('\033[0;31m', end=' ')
    print('{} '.format(c), end=' ')

print('\n\033[mO número {}, foi divisível {} vezes'.format(n,div))
if div == 2:
    print('E por isso ele é primo!')
else:
    ('E por isso, ele NÃO é primo!')