p = float(input('Qual o preço do produto? '))
d = p - (p * 5/100)
print('O produto que custava {}, na promoção com 5% de desconto vai custar R${:.2f}'.format(p,d))