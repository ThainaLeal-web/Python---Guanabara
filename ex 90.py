dic = {}
nome = input('Nome: ')
dic["Nome"]= nome
media = float(input(f'Média de {nome}: '))
dic["Media"]= media
if media >= 7:
    sit = 'Aprovado'
else:
    sit = 'Reprovado'
dic["Situação"]= sit
for k, v in dic.items():
    print(f'{k} é igual a {v}')
