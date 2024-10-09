from datetime import date
ano = int(input('Ano de nascimento: '))
anoa = date.today().year
idade = anoa - ano

print('Quem nasceu em {} tem {} anos'.format(ano,idade))
if idade == 18:
    print('Este é o ano do alistamento!!')
elif idade <18:
    print('Ainda faltam {} anos para o alistamento!'.format(18 - idade))
    print('O seu alistamento será em: {}'.format(anoa + (18 - idade)))
elif idade > 18:
    print('Você já deveria ter se alistado!')
    print('Seu alistamento foi em {}'.format(anoa - (idade - 18)))