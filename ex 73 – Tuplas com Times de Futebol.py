camp = ['PALMEIRAS', 'GRÊMIO', 'ATLÉTICO-MG', 'FLAMENGO', 'BOTAFOGO', 'RED BULL BRAGANTINO', 'FLUMINENSE', 'ATHLETICO-PR', 'INTERNACIONAL', 'FORTALEZA', 'SÃO PAULO', 'CUIABÁ', 'CORINTHIANS', 'CRUZEIRO', 'VASCO', 'BAHIA', 'SANTOS', 'GOIÁS', 'CORITIBA', 'AMÉRICA-MG']
print('-='*10)
print(f'Os 5 primeiros são: {camp[:5]}')
print('-='*10)
print(f'Os 4 últimos são: {camp[-4:]}')
print('-='*10)
print(f'Times em ordem alfábética {sorted(camp)}')
print('-='*10)
print(f'O Botafogo está na posição {camp.index("BOTAFOGO")+1}')
