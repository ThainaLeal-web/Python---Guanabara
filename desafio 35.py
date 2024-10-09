print('-='*20)
print('Analisador de triângulo')
print('-='*20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if (n2 - n3) < n1 < n2 + n3 and ( n1 - n3 ) < n2 < n1 + n3 and ( n1 - n2 ) < n3 < n1 + n2:
    print('Os seguimentos acima PODEM formar um triângulo!')
else:
    print('os segmentos acima NÃO podem formar um triângulo!')