n = int(input('Digite um número inteiro: '))
print('[1] Converter para BINÁRIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
op = int(input('Sua escolha: '))
if op == 1:
    print('O número {} em binário é {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('O número {} em OCTAL é {}'.format(n,oct(n)[2:]))
elif op == 3:
    print('O número {} em HEXADECIMAL é {}'.format(n,hex(n)[2:]))
else:
    print('Escolha inexistente')