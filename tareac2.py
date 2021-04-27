#1. Crear un nuevo repositorio
#2. Tomar de base el programa de la clase pasada
#3. Vamos a modificar el programa para que solo tome como válidos números entre 1 y 120
# (si pone un número entre -inf y 0 o 121 a inf debe volver a preguntar)
#3. Al inicio del programa preguntar cuantas personas registrar
#4. Hacer que el programa que se hizo se ejecute esas n veces que se pusieron en el punto 3
#5. Subir el programa al repositorio creado.

clientes = int(input('Ingrese número de clientes: '))
for i in range(clientes):
    print(i)
    edad = 0
    check_edad = False
    while edad <1 or edad>120:
        edad = int(input('Digame su edad: '))
    if edad<0:
        print('Usted no nació')
    elif edad <18:
        print('Usted es menor de edad')
    elif edad <65:
        print('Usted es mayor de edad')
    else:
        print('Usted es jubilado')
