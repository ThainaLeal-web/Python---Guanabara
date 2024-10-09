print('Gerador de PA')
#print(-=*10)
c = 1
contt = 0

pt = int(input('Primeiro termo: '))
rp = int(input('Razão da PA: '))

print(pt, '->', end=' ')

contt += 10

while c < 10:
    pt + rp
    c += 1
    r = pt+rp
    print(r, '->',end=' ' )
    pt = r

print('PAUSA')
resp=int(input('Quantos termos você quer mostrar a mais? '))

while resp != 0:
    contt += resp
    c = 1
    for c in range (1, resp+1):
        c += 1
        r = r + rp
        print(r, '->', end=' ')
    print('PAUSA')
    resp = int(input('Quantos termos você quer mostrar a mais? '))
else:
    print('Progressão finalizada, com {} termos mostrados!'.format(contt))

