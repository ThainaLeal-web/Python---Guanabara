from datetime import date
toti = 0
totm= 0
for c in range(1,8):
    n = int(input('Em que ano a {}°  pessoa nasceu? '.format(c)))
    i = date.today().year - n
    if i >= 18:
        toti += 1
    else:
        totm += 1

print('Das 7 pessoas analisadas {} são maiores de 18 \n E, {} são menores.'.format(toti, totm))