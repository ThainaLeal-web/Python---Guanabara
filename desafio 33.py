n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o Segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 < n2 and n1 < n3:
    nmenor = n1
else:
    nmenor = n2
if nmenor > n3:
    nmenor = n3
print('O menor número digitado é: {}'.format(nmenor))

#CALCULAR O MAIOR NÚMERO

if n1 > n2 and n1 > n3:
    nmaior = n1
else:
    nmaior = n2
if nmaior < n3:
    nmaior = n3
print('O maior número digitado foi {}'.format(nmaior))