# DEFINIR LAS CANCIONES
canciones = {
    'brr' : ['fiu', 'cric-cric', 'brrah'],
    'birip' : ['trri-trri', 'croac'],
    'plop' : ['cric-cric', 'brrah'],
    'croac': [],
    'brrah' : [],
}

# FUNCIÓN
def reproducir_cancion(sonido):
    if sonido in canciones:
        cancion = canciones.get(sonido, [])
        for s in cancion:
            print(s)
    else:
        print ('Sonido no reconocido.')


sonido = input('Ingresa un sonido: ')
reproducir_cancion(sonido)
