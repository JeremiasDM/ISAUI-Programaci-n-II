"""""
5. Eliminar duplicados: Crea una función que tome una lista y devuelva una nueva lista
sin elementos duplicados.
"""""

def eliminar_duplicados(lista):
    return list(set(lista))

numeros = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(eliminar_duplicados(numeros))  
