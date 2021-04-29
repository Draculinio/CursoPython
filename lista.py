color1 = 'azul'
color2 = 'verde'
color3 = 'rojo'

colores = ['azul', 'verde', 'rojo']
print(colores)
print(colores[1])

print(len(colores))

#for i in range(0,len(colores)):
#    print(colores[i])

for color in colores:
    print(color)

colores.append('rosa')
print(colores)
colores.insert(2, 'celeste')
print(colores)
colores.pop()
print(colores)
colores.pop(2)
print(colores)
colores.reverse()
print(colores)
colores.sort()
print(colores)
colores_dos = ['naranja', 'violeta', 'marrón']
colores.extend(colores_dos)
print(colores)

colores_tres = colores
colores_tres[1] = 'Negro'
print(colores_tres[1])
print(colores[1])
colores_cuatro = colores.copy()
colores_cuatro[1] = 'Blanco'
print(colores_cuatro[1])
print(colores[1])
colores.clear()
print(colores)

#cosas = [1, False, "amarillo", 5.23, ['Hola','Chau','Coso', ['perro', 'gato', []]]]
#print(cosas)
#print(cosas[4][0])
