from time import sleep
c = 0
def contagem(i,f,passo):
    print('=-' * 30)
    print(f'Contagem de {i} até {f} de {passo} em {passo}')
    if i < f:
        for c in range (i,f+1,passo):
            print(c, end=' ')
            c += 1
        print('Fim!')

    else:
        while i > f:
            print(i,end=' ')
            i -= passo
        print('FIM!')

contagem(1,10,1)
contagem(10,0,2)
print('=-' * 30)
print('Agora é a sua vez de personalizar a contagem!')
ip = int(input('Início: '))
fp = int(input('Fim: '))
pp = int(input('Passo: '))
contagem(ip,fp,pp)