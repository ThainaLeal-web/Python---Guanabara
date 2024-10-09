import time
import random

c = random.randrange(0,11) #número aleatório do computador
cont = 1

print('Sou o seu computador...')
print('Acbei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?!')
time.sleep(1)
p = int(input('Qual o seu palpite? '))

while p != c:
    cont += 1
    if c > p:
        p = int(input('Mais...Tente mais uma vez: '))
    elif c < p:
        p = int(input('Menos... Tente mais uma vez: '))
if p == c:
    print("Parabéns! Você acertou com {} tentativas".format(cont))
