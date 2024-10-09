def area(largura,comp):
    print(f'A area de um terreno {largura}x{comp} é de {largura*comp}!')


print('Controle de terrenos')
print('---'*30)
largura = float(input('Largura (m): '))
comp = float(input('Comprimenro (m): '))
area(largura,comp)
