from datetime import date
ano = int(input('Qual ano deseja analisar? Digite 0 para analisar o ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano%400 == 0:
    print ('O ano de {}, é BISSEXTO'.format(ano))
else:
    print ('O ano de {}, NÃO é bissexto'.format(ano))