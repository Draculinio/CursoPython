#Este es un programa de prueba para el curso de Python
#print('Hola mundo')
#edad = 21
edad = input('Digame su edad: ')
#print(edad)
#print(type(edad))
edad = int(edad)
#if edad >= 18:
#    print('Usted es mayor de edad')
#    if edad == 65:
#        print('Prepare sus trámites de jubilación')
#else:
#    print('Usted es menor de edad')

if edad<0:
    print('Usted no nació')
elif edad <18:
    print('Usted es menor de edad')
elif edad <65:
    print('Usted es mayor de edad')
elif edad <120:
    print('Usted es jubilado')
else:
    print('Usted está en el otro mundo')

a = 'Hola'
b = 'mundo'

print(a+' '+b+' que tal')
