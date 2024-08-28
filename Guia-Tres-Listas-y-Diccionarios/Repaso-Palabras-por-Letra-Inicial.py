"""
Palabras por letra inicial : Escribe una función que tome una lista de palabras y devuelva un diccionario donde las claves son las letras iniciales
de las palabras y los valores son listas de palabras que comienzan con esa letra.
"""

def agrupar_por_letra_inicial(palabras):
    diccionario = {}
    for palabra in palabras:
        letra_inicial = palabra[0].lower()
        if letra_inicial not in diccionario:
            diccionario[letra_inicial] = []
        diccionario[letra_inicial].append(palabra)
    return diccionario

lista_palabras = ["manzana", "mango", "pera", "plátano", "melón", "papaya", "arándano"]
resultado = agrupar_por_letra_inicial(lista_palabras)
print(resultado)