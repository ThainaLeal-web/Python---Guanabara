from time import sleep

def maior(*num):
    c = nmaior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        sleep(0.4)
        c += 1
    print(f'Foram informados {c} números ao todo!')
    if nmaior == 0:
        n = nmaior
    else:
        nmaior = n
    print(f'O maior número informado foi {nmaior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()