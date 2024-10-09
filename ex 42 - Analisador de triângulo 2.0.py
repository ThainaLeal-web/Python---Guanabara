print('-='*20)
print('Analisador de triângulo')
print('-='*20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if (n2 - n3) < n1 < n2 + n3 and ( n1 - n3 ) < n2 < n1 + n3 and ( n1 - n2 ) < n3 < n1 + n2:
    print('Os seguimentos acima PODEM formar um triângulo!')
    if n1 == n2 == n3:
        print('Todos os lados são iguais, é um triângulo EQUILÁTERO!')
    elif n1 == n2 != n3 or n1 == n3 != n2 or n3 == n2 != n1:
        print('Dois lados são iguais, é um triângulo ISÓSCELES!')
    else:
        print('Todos os lados são diferentes, é um triângulo ESCALENO!')
else:
    print('os segmentos acima NÃO podem formar um triângulo!')
