""""
Ejercicio 7
Contar letras: Crea una función que tome una cadena como entrada y devuelva un
diccionario con el recuento de cada letra en la cadena.
"""

def contar_letras(cadena):
    contador = {}
    for letra in cadena:
        if letra.isalpha():
            contador[letra] = contador.get(letra, 0) + 1
    return contador

cadena = input("Introduce una cadena de texto: ")
print(contar_letras(cadena))

