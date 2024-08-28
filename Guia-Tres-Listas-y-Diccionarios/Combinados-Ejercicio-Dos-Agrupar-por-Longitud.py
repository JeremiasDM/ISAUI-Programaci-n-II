"""""
2. Agrupar por longitud: Escribe una función que reciba una lista de palabras y devuelva
un diccionario donde las claves son las longitudes de las palabras y los valores son
listas de palabras con esa longitud.
"""""

def agrupar_por_longitud(palabras):
    grupos = {}
    for palabra in palabras:
        longitud = len(palabra)
        if longitud not in grupos:
            grupos[longitud] = []
        grupos[longitud].append(palabra)
    return grupos

palabras = ["uno", "dos", "tres", "cuatro", "cinco"]
print(agrupar_por_longitud(palabras))
