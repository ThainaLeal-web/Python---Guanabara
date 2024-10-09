jogador = {}
time = []
gols = []

while True:
    gols.clear()
    c = i = 0
    jogador['Nome'] = input('Nome do jogador: ')
    part = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    if part != 0:
        while c < part:
            c+=1
            gol = int(input(f'   Quantos gols na partida {c}? '))
            gols.append(gol)
        jogador['Gols'] = gols
    time.append(jogador.copy())
    while True:
        resp = input('Deseja continuar? [S/N]' ).upper() [0]
        if resp in 'SN':
            break
        print('ERRO! Digite somente S ou N')
    if resp == 'N':
        break

print(jogador)
print(time)


