n = int(input('Digite um número [999 para parar]: '))
c = 0
ns = 0
while n != 999:
    ns += n
    c+= 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(c,ns))
