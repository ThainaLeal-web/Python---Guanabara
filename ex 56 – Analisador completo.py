soma = 0
mnovas = 0
idadehv = 0
nomehm = (' ')

for c in range(1, 5):
    print('----- {}° PESSOA -----'.format(c))
    n = input('Nome: ')
    i = int(input('Idade: '))
    s = str(input('Sexo F/M: ').upper())[0]
    soma = soma + i
    if i < 20 and s == 'F':
        mnovas += 1
    elif s == 'M' and i > idadehv:
        nomehm = n
print('A média de idade do grupo é de: {}'.format(soma/c))
    if mnovas == 0:
        print('Não há mulheres menores de 20 anos')
    else:
    print('O total de mulher com menos de 20 anos é {}'.format(mnovas))
print('O nome do homem mais velho é: {}'.format(nomehm))
