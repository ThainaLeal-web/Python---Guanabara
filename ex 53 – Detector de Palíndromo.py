p = input('Digite uma frase: ').strip().upper().split()
p1 = ''.join(p)
pinv = p1[::-1]
print('A frase {} invertida é {}'.format(p1, pinv))
if pinv == p1:
    print('A frase digitada é um \033[:34mPALÍNDROMOS\033[m')
else:
    print('A frase digitada \033[:31mNÃO\033[m é um palíndromos')
