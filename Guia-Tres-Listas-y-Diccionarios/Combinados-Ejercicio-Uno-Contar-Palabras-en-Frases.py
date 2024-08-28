"""""
1. Contar palabras en frases: Escribe una función que reciba una lista de frases y
devuelva un diccionario donde las claves son las palabras y los valores son las
frecuencias de esas palabras en todas las frases.
"""""

def contar_palabras(frases):
    frecuencias = {}
    for frase in frases:
        palabras = frase.split()
        for palabra in palabras:
            palabra = palabra.lower()
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

frases = ["Hola mundo", "Python", "Desarollo de Software", "Desarollo Web"]
print(contar_palabras(frases))

