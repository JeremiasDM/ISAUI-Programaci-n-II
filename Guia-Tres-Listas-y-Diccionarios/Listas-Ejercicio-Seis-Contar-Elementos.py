"""""
6. Contar elementos: Escribe una función que reciba una lista y un valor, y devuelva
cuántas veces aparece ese valor en la lista.
"""""

def contar_elementos(lista, valor):
    return lista.count(valor)

numeros = [1, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4, 5]
print(contar_elementos(numeros, 2))