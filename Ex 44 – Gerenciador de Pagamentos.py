v = float(input('Qual o valor do produto? R$' ))
print ('''[1] Dinheiro/cheque
[2] Cartão''')
p = int(input('Qual a forma de pagamento? '))
if p == 2:
    pc = int(input(('''O parcelamento seria em quantas vezes?
    [1] 1x
    [2] 2x
    [3] 3x ou mais
    ''')))
    if pc == 1:
        print('O valor do produto sai por R${}'.format(v - (v * 5/100)))
    elif pc == 2:
        print('O valor do produto sai por R${}'.format(v))
    elif pc == 3:
        print('O valor do produto sai por R${}'.format(v + (v * 20/100)))
    else:
        print('Opção invalida. Tente novamente!')

elif p == 1:
    print('O valor do produto sai por R${}!'.format(v - (v * 10/100)))
else:
    print('Erro: Tente novamente!')