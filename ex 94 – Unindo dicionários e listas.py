#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa = {}
comunidade = []
tot = 0
mulheres = []
idade_acima = []

while True:
    pessoa['Nome'] = input('Nome: ')
    while True:
        pessoa['Sexo'] = input('Sexo: [F/M] ').upper()[0]
        if pessoa['Sexo'] in 'FM':
            break
        print('Erro! Responda apenas F/M')
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])
    pessoa['Idade'] = int(input('Idade: '))
    comunidade.append(pessoa.copy())
    tot += pessoa['Idade']
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in "SN":
            break
        print('Erro! Responda apenas S ou N!')
    if resp == 'N':
        break
for pessoa in comunidade:
    if pessoa['Idade'] > (tot/len(comunidade)):
        idade_acima.append(pessoa['Nome'])

print('-='*30)
print(f'Ao todo temos {len(comunidade)} pessoas cadastradas')
print(f'Média das idades: {tot/len(comunidade):5.2f}')
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'Essas pessoas estão com idade acima da média {idade_acima}')
