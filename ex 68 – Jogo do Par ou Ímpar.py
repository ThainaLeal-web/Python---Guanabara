import random

print('-='*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*20)
c = p = 0
while True:
    v = int(input('Diga um número: '))
    pi = input('par ou impar [PAR/IMPAR]: ').upper()
    print('--'*20)
    pc = random.randrange(1,10)
    soma = pc + v
    if soma % 2 == 0:
        deu = ('PAR')
    else:
        deu = ('IMPAR')
    print(f'Você jogou {v} e o computador {pc}. Total de {(soma)} DEU {deu}')
    if pi == deu:
        print('Você ganhou!')
        c += 1
        print('--' * 20)
    else:
        print('Você perdeu!')
        print('--' * 20)
        break
print(f'GAME OVER! Você venceu {c} vezes')