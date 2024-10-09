dados = []
pacientes = []

while True:
    dados.append(input('Nome do paciente: '))
    dados.append(int(input('Peso do paciente kg ')))
    print(dados[:1])
    print(dados[1:2])
    if len(pacientes) == 0:
        maior = menor = dados[:1]
    else:
        if dados[1:2] > maior:
            maior = dados[:2]
        elif dados[1:2] < menor:
            menor = dados[:2]
    pacientes.append(dados[:])
    dados.clear()
    resp = input('Deseja adicionar mais um cliente? [S/N] ').upper()[0]
    if resp == 'N':
        break
    while resp != 'S':
        print('ERROR')
        resp = input('Deseja adicionar mais um cliente? [S/N] ').upper()[0]
        if resp == 'N':
            break
print(f'O total de clientes cadastrados é {len(pacientes)}')
print(f'O maior peso: {maior}kg ')
print(f'O menor peso: {menor}kg')