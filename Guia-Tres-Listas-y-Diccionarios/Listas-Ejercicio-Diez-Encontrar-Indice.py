"""""
10.Encontrar índice: Escribe una función que reciba una lista y un valor, y devuelva el
índice de la primera aparición de ese valor en la lista, o -1 si el valor no está presente.
"""""

def encontrar_indice(lista, valor):
    return lista.index(valor) if valor in lista else "No es un Valor dentro de la lista" 

numeros = [1, 2, 3, 4, 5]
print(encontrar_indice(numeros, 3))
print(encontrar_indice(numeros, 10))  
