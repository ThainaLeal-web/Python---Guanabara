n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('A média do aluno é de {}'.format(m))
if m >= 7:
    print('O aluno está \033[1;30;42mAPROVADO\033[m!')
elif m >= 5 and m < 7:
    print('O aluno está em \033[1;30;43mRECUPERAÇÃO\033[m!')
else:
    print('O aluno está \033[1;30;41mREPROVADO\033[m!')
