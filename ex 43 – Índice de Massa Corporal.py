p = float(input('Qual o seu peso? '))
a = float(input('E, qual a sua altura? '))
imc = p / (a *a )
print ('O seu imc é de {:.1f} kg/m2'.format(imc))
if imc <18.5:
    print('O seu imc está abaixo do peso ideal!')
elif imc >=18.5 and imc <25:
    print('O seu imc está no peso ideal! Parabéns!')
elif imc >=25 and imc <30:
    print('Você está com sobrepeso')
elif imc >=30 and imc < 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida. Cuidado!')