"""""
Ejercicio 9
Ordenar lista de cadenas: Escribe una función que tome una lista de cadenas y devuelva una
lista ordenada alfabéticamente de esas cadenas, ignorando mayúsculas y minúsculas.
"""""

def ordenar_cadenas(lista):
    return sorted(lista, key=str.lower)

cadenas = input("Introduce cadenas separadas por comas: ").split(', ')
print("Lista ordenada:", ordenar_cadenas(cadenas))
