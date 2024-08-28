"""""
Ejercicio 4: Contador de Palabras
Desarrolla un programa en Python que solicite al usuario que ingrese una frase y luego cuente y muestre el número de palabras en esa frase.
"""""

def contar_palabras(frase: str) -> int:
    palabras = frase.split()
    return len(palabras)

Frase = input("Ingrese una frase: ")
NumeroDePalabras = contar_palabras(Frase)
print("La Frase: ", Frase, "Contiene", NumeroDePalabras, "Palabras")

