"""""
9. Actualizar diccionario: Escribe una función que tome un diccionario y una lista de
tuplas (clave, valor) y actualice el diccionario con esas tuplas.
"""""

def actualizar_diccionario(dic, tuplas):
    for clave, valor in tuplas:
        dic[clave] = valor
    return dic

dic = {'a': 1, 'b': 2}
tuplas = [('a', 3), ('c', 4)]
print(actualizar_diccionario(dic, tuplas))
