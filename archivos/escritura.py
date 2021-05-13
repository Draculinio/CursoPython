f = open('mi_archivo.txt','w')

miLista = ['Hola\n', 'Vamos Racing\n', 'Asi estamos\n']

f.write('Hola HOLA')

f.writelines(miLista)

f.close()

arch = 'pepito5132021.txt'
f = open(arch, 'w')
f.write('Hola HOLA')
f.close()
