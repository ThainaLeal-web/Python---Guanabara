def ficha(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '' or ' ':
    ficha(gols=gols)
else:
    ficha(nome,gols)

