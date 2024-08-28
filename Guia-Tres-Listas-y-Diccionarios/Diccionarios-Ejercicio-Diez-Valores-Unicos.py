"""""
10.Valores únicos: Escribe una función que reciba un diccionario y devuelva una lista de
valores únicos en el diccionario.
"""""

def valores_unicos(dic):
    return list(set(dic.values()))

dic = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
print(valores_unicos(dic))
