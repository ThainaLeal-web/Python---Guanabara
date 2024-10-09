exp = input('Digite uma expressão: ')
pilha = []
for l in len(exp):
    if l == '(':
        pilha.append('(')
    elif l == (')'):
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está inválida!')
    