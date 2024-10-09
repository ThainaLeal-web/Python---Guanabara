import random
import time
from operator import itemgetter
c = i = 1
jogadores = {}
ranking = {}

for c in range(4):
    resultado = random.randint(1, 6)
    print(f'O jogador {c+1} tirou {resultado}')
    time.sleep(1)
    c += 1
    jogadores[f"Jogador{c}"] = resultado
print('-='*30)
print('Ranking dos jogadores:')
print('-='*30)
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse=True)
for k, v in ranking:
    time.sleep(1)
    print(f'{i}° Lugar: {k} com {v}')
    i += 1
