import random
from time import sleep

numeros = []

def sorteia(*num):
    print('Sorteando 5 valores da lista: ', end=' ')
    for n in range(0,5):
        n = random.randint(1,100)
        print(n, end=' ')
        sleep(0.4)
        numeros.append(n)
    print('Pronto!')

def somapar(*num):
    s = 0
    print(f'Somando os valores pares de {numeros}', end=' ')
    for n in numeros:
        if n % 2 == 0:
            s += n
    print(f', temos {s}')


sorteia()
somapar()

