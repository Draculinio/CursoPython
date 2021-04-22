clientes = int(input('Ingrese número de clientes: '))
for i in range(clientes):
    print(i)
    edad = int(input('Digame su edad: '))
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
        break
else:
    print('Proceso de carga finalizado')
