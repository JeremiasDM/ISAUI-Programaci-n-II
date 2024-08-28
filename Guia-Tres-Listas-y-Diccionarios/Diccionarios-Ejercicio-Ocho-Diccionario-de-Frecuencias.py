"""""
8. Diccionario de frecuencias: Escribe una función que reciba una lista de palabras y
devuelva un diccionario con la frecuencia de cada palabra.
"""""

def diccionario_frecuencias(lista):
    frecuencia = {}
    for palabra in lista:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

lista_palabras = ["hola", "mundo", "hola", "python"]
print(diccionario_frecuencias(lista_palabras))