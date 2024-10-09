s = float(input('Qual o salario do funcionario? R$'))
if s <= 1250:
    satual = (s * 15/100) + s
else:
    satual = (s * 10/100) + s
print('Quem ganhava R${}, passa a receber R${} agora'.format(s,satual))