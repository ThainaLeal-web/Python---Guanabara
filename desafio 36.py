vimovel = float(input('Qual o valor do imóvel: R$'))
scliente = float(input('Qual o salário do comprador? R$'))
fanos = int(input('Quantos anos de financiamento? '))
mensal = (vimovel / fanos) / 12
print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(vimovel, fanos, mensal))
if (mensal < (scliente*30)/100):
    print('Empréstimo \033[0:30:42mAPROVADO\033[m, parabéns!!')
else:
    print( 'Empréstimo \033[0:30:41mNEGADO\033[m. Tente aumentar a quantidade de anos.')