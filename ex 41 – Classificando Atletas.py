from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('A sua categoria é: MIRIM')
elif idade <= 14:
    print('A sua categoria é: INFANTIL')
elif idade <= 19:
    print('A sua categoria é: JÚNIOR')
elif idade <=25:
    print('A sua categoria é: SÊNIOR')
else:
    print('A sua categoria é: MASTER')
