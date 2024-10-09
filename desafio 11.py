l = float(input('Largura da parede: '))
c = float(input('Altura da parede: '))
a = l*c
t = a/2
print('Sua parede tema  dimensão de {} x {}, e sua área é de {}m².'.format(l,c,a))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(t))