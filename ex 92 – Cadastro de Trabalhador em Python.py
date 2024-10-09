from datetime import date

contratação = {}
n = input('Nome: ')
contratação['Nome'] = n
nasc = int(input('Ano de nascimento: (aaaa)'))
contratação['Idade'] = (date.today().year - nasc)
trab = input('carteira de trabalho: (0 não tem) ')
contratação['CTPS'] = trab
if trab != '0':
    anocont= int(input('Ano de contratação: '))
    contratação['Contratação '] = anocont
    sal = int(input('Salário: '))
    contratação['Salário'] = sal
    contratação['Aposentadoria'] = ((contratação['Contratação '] + 35) - date.today().year)

print('-=' *30)
for k, v in contratação.items():
    print(f'- {k} tem o valor {v}')