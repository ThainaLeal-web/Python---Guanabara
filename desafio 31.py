d = float(input('Qual a distância da sua viagem, em KM? '))
print('Você está prestes a começar uma viagem de {} KM!'.format(d))
if d <= 200:
    p = d*0.50
else:
    p= d*0.45
print('E o preço da sua passagem será de R${}'.format(p))