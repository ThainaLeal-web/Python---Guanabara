def voto():
    from datetime import date
    ano = int(input('Em que ano você nasceu? '))
    idade = date.today().year - ano
    if idade >= 18:
        print('OBRIGATÓRIO nas eleições')
    elif 16 <= idade < 18:
        print('OPCIONAL nas eleições')
    else:
        print('NEGADO nas eleições')


voto()
