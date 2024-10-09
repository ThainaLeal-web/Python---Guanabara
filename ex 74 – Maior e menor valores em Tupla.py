import random
nmaior = 0
nmenor = 100000000000000000000000
x = [random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)]

print(f'Os valores sorteados foram: {x}')
print(f'O maior valor sorteado foi {sorted(x)[-1]}')
print(f'O menor valor sorteado foi {sorted(x) [0]}')

