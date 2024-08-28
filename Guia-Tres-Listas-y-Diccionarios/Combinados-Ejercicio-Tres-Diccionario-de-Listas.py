"""""
3. Diccionario de listas: Escribe una función que tome un diccionario donde los valores
son listas y devuelva una lista que contenga todos los elementos de las listas del
diccionario.
"""""

def diccionario_a_lista(dic):
    elementos = []
    for lista in dic.values():
        elementos.extend(lista)
    return elementos

dic = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6, 7, 8]}
print(diccionario_a_lista(dic))  
