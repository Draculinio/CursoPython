jugador = {
    'nombre': 'Ruben',
    'apellido': 'Paz',
}


#jugadores = [

    #{'nombre': 'algo',
    #'apellido':'algo'},
    #{'nombre': 'algo2',
    #'apellido':'algo2'}

#]

otros_clubes = {

    'clubes': ['Racing', 'Peñarol','Internacional','Racing París', 'Genoa']

}

jugador.update(otros_clubes)

jugador['goles'] = 150

jugador['goles'] = 200

print(jugador)

print(jugador.values())

print(jugador.keys())

jugador.clear()
print(jugador)
