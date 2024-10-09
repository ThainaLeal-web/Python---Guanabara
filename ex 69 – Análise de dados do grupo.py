idm = 0 # quantos homens foram cadastrados.
h = 0 # quantos homens foram cadastrados.
mm = 0 #quantas mulheres tem menos de 20 anos

while True:
    print('---'*10)
    print('    CADASTRE UMA PESSOA')
    print('---' * 10)
    id = int(input('Idade: '))
    while id > 122:
        print('Idade inválida')
        id = int(input(('Idade: ')))
    if id > 18:
            idm += 1
    se = input('Sexo: [F/M] ').upper()
    if se == 'F' or se == 'M':
        print('Sexo cadastrado com sucesso')
    elif se != 'F' or se != 'M':
        print('Sexo inválido')
        se = input('Sexo: [F/M] ').upper()
    if se == 'M':
        h += 1
    print('---' * 10)
    if id < 20 and se == 'F':
        mm += 1
    es = input('Quer continuar? [S/N] ').upper()
    while es not in 'SN':
        print('Escolha inválida!')
        es = input('Quer continuar? [S/N] ').upper()
    if es == 'N':
        break

print(f'O total de pessoas com mais de 18 anos é: {idm}')
print(f'Ao todo temos {h} homem (s) cadastrado (s)')
print(f'E temos {mm} mulheres com menos de 20 anos')