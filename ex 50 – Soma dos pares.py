s = 0
for c in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s= n + s
print('A soma dos números pares ditados correspodnem a: {}'.format(s))