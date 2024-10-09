c=0
ns=0
nm=0
m = float(0)

n = int(input('Digite um número: '))
r = input('Quer continuar? [S/N] ').upper()
nmenor=n

c += 1
ns += n

if n > nm:
    nm = n
elif n < nmenor:
    nmenor = n

while r != 'N':
    n = int(input('Digite um número: '))
    r = input('Quer continuar? [S/N] ').upper()
    if n == n:
        nm = nmenor = n
    else:
        if n>nm:
            nm = n
        elif n<nmenor:
            nmenor = n
    c += 1
    ns += n

m = ns / c

print('Você digitou {} números e média foi {}'.format(c,m))
print('O maior valor foi {} e o menor {}'.format(nm, nmenor))