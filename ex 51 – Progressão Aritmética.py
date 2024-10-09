#print(-=*20)
#print('            10 TERMO DE UMA PA            ')

t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = t + (10-1) * r
for c in range(t,d,r):
    print(c)
print('Acabou')