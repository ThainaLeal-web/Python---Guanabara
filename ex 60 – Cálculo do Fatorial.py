n = int(input('Digite um número, para calcular a sua fatorial: '))
c = 1
c2 = n
r = n
while c in range(1,n):
    r *= c
    c+=1

print('Calculando {}! = '.format(n), end=' ')
while c2 > 0:
    print('{}'.format(c2), end=' ')
    print(' x ' if c2 > 1 else ' = ', end = ' ')
    c2-= 1

print(r)