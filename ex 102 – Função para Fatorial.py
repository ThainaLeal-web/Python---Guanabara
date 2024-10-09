def fatorial(n,show = False):
    f = 1
    if show == True:
        for i in range(n, 0, -1):
            f *= i
            if i == 1:
                print(f'{i} =', end=' ')
            else:
                print(f'{i} x', end=' ')
        return f
    else:
        for i in range(n, 0, -1):
            f *= i
        return f

n = int(input('Digite um número: '))
#show = input('Deseja mostrar a conta? True/false ')
print(fatorial(n))
