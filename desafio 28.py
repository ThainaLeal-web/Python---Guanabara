import random
print('Estou pensando em um número de 0 a 5!')
comp = random.randint(0,5)
nu = int(input('Em qual número eu pensei? '))
if nu == comp:
    print('Parabéns, você acertou!')
else:
    print('Você errou! Tente novamente!')