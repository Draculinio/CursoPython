lorem = open('lorem.txt','r')

#LEER ARCHIVO
#print(lorem.read())
#print(lorem.read(12))

#Linea a linea
#linea = lorem.readline()
#print(linea)
#linea = lorem.readline()
#print(linea)

#linea = lorem.readline()
#while linea != '':
#    print(linea)
#    linea = lorem.readline()

#for linea in lorem:
#    print(linea, end='')

#Convertir archivo en lista
#texto = lorem.readlines()
#print(texto)

texto = list(lorem)
print(texto)
