"""""
Ejercicio 8
Palíndromo: Escribe una función que determine si una palabra o frase es un palíndromo (se
lee igual de adelante hacia atrás que de atrás hacia adelante), ignorando espacios y signos
de puntuación.
"""""

def es_palindromo(frase):
    frase = ''.join(c.lower() for c in frase if c.isalnum())
    return frase == frase[::-1]

frase = input("Introduce una palabra o frase: ")
print("Es un palíndromo" if es_palindromo(frase) else "No es un palíndromo")
