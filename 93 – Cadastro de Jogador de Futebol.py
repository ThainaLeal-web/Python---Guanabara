c = soma = i = 0

jogador = {}
gols = []

n = input('Nome do jogador: ')
jogador['Nome'] = n
part = int(input(f'Quantas partidas {n} jogou? '))
if n != 0:
    while c < part:
        c+=1
        gol = int(input(f'   Quantos gols na partida {c}? '))
        soma += gol
        gols.append(gol)
jogador['Gols'] = gols
jogador['Total'] = soma
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {n} jogou {part} partidas.')
while i != part:
    print(f'   => Na partida {i+1}, fez {gols[i]} gols')
    i+=1