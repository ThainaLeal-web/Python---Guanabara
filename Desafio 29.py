v = int(input('Qual a velocidade atual do veículo? ' ))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h')
    print('Você deve pagar uma multa de R${}'.format((v - 80) * 7))
print('tenha um bom dia! Dirija com segurança!')