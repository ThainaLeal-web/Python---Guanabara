from random import sample
import time
cont = 0
print('-'*30)
print('Joga na mega sena'.center(30))
print('-'*30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= Sorteando {n} jogos -=-=-=')
while cont < n:
    x = sample(range(0, 101), 6)
    time.sleep(1)
    x.sort()
    print(f'Jogo {cont+1}: {x}')
    cont += 1
print('-=-=-=-=< BOA SORTE >-=-=-=-=-=')


