c = r = 0
while True:
    print('--' * 20)
    n = int(input('Deseja ver a tabuada de qual número? '))
    print('--' * 20)
    if n < 0:
        break
    for c in range(1,10):
        r = c * n
        print(f'{c} * {n} = {r}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')