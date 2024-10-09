

print('---'*10)
print('Sequência de fibonacci')
print('---'*10)
n = int(input('Quantos termos você quer mostrar? '))
print('~~~~'*10)
print('0 -> 1', end=' -> ')

n1 = 0
n2 = 1
c= 0

while c < n-2:
    n3 = n1 + n2
    print(n3, end=' -> ')
    n1=n2
    n2=n3
    c += 1

print('FIM')
print('~~~~'*10)
