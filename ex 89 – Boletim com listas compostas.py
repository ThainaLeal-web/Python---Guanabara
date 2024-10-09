alunos = []
cont = c = 0
while True:
    n = input('Qual o nome do aluno? ')
    not1 = float(input('Nota 1: '))
    not2 = float(input('Nota 2: '))
    media = float((not1 + not2) / 2)
    cont += 1
    alunos.append([n,not1,not2,media])
    resp=input('Quer continuar? [S/N] ').upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'{"No.":<4} {"Nome":<10} {"Média":>8}')
print('--'*25)
for i in range(cont):
    print(f'{i:<4} {alunos[i][0]:<10} {alunos[i][3]:>8}')

    i=+1
print('--'*25)
while True:
    resp = int(input('Mostrar notas de qual aluno? (999 - interrompe) '))
    if resp == 999:
        break
    elif resp > cont or resp < 0:
        print('Escolha inválida!')
    else:
        print(f'Notas de {alunos[resp][0]} são {alunos[resp] [1]}, {alunos[resp] [2]} ')

