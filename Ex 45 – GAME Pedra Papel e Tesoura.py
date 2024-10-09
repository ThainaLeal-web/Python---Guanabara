import random
import time

print('''Suas opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
e = int(input('Qual a sua escolha? '))

if e ==1:
    e = ('PEDRA')
elif e == 2:
    e = ('PAPEL')
elif e == 3:
    e = ('TESOURA')
else:
    print('Escolha invalida! Tente novamente.')

lista = ['PEDRA' , 'PAPEL', 'TESOURA']
comp = random.choice(lista)

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)

print(('-=') * 20)
print('Jogador jogou: {}'.format(e))
print('Computador jogou: {}'.format(comp))
print(('-=') * 20)

#Pedra empata com Pedra e ganha de Tesoura.
#Tesoura empata com Tesoura e ganha de Papel
#Papel empata com Papel e ganha de Pedra

if e == ('PEDRA') and comp == ('PEDRA') or e == ('TESOURA') and comp == ('TESOURA') or e == ('PAPEL') and comp == ('PAPEL'):
    print('Ninguém ganhou! Empate!')
elif e == ('PEDRA') and comp == ('TESOURA') or e == ('TESOURA') and comp == ('PAPEL') or e == ('PAPEL') and comp == ('PEDRA'):
    print ('TEMOS UM VENCEDOR!')
    time.sleep(1)
    print('O jogador ganhou!!')
elif comp == ('PEDRA') and e == ('TESOURA') or comp == ('TESOURA') and e== ('PAPEL') or comp == ('PAPEL') and e == ('PEDRA'):
    print ('TEMOS UM VENCEDOR!')
    time.sleep(1)
    print('A MAQUINA ganhou!!')
