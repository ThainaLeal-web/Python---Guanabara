nome = ['ZERO', 'UM','DOIS', ' TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', ' OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE','VINTE']
n = int(input('Digite um número de 0 a 20: '))
while True:
    if n <= 20 and n >= 0:
        break
    else:
        print('Tente novamente!')
        n = int(input('Digite um número de 0 a 20: '))
print(f'Você digitou o número: {nome[n]}')