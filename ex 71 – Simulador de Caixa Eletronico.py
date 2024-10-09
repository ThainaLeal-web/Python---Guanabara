print('==='*10)
print('          BANCO TCL')
print('==='*10)
c = 0
c50 = 0
n1 = 0
c2 = 0
n2 = 0
c10 = 0
c1 = 0
c3 = 0

val = int(input('Qual valor deseja sacar? R$'))

if val >= 50:
    while c50 != val and c50 + 50 <= val:
        c +=1
        c50 += 50
        n1 = val - c50
    while c10 != n1 and c10 + 10 <= n1:
        c2 += 1
        c10 += 10
        n2 = n1 - c10
    while c1 != n2 and c1 + 1 <= n2:
        c3 += 1
        c1 += 1

elif val < 50 and val >= 10:
    while c10 != val and c10 + 10 <= val:
        c2 += 1
        c10 += 10
        n2 = val - c10
    while c1 != n2 and c1 + 1 <= n2:
        c3 += 1
        c1 += 1
else:
    while c1 != val and c1 + 1 <= val:
        c3 += 1
        c1 += 1



print(f'Total de {c} cédulas de R$50')
print(f'Total de {c2} cédulas de R$10')
print(f'Total de {c3} cédulas de R$1')
print('==='*10)
print('Volte Sempre! BANCO TCL. Tenha um ótimo dia!')