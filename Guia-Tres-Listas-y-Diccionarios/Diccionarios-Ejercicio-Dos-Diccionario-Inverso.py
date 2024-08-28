"""""
2. Diccionario inverso: Escribe una función que tome un diccionario y devuelva uno
nuevo que invierta las claves y los valores.
"""""

def diccionario_inverso(dic):
    return {valor: clave for clave, valor in dic.items()}

dic = {'a': 1, 'b': 2, 'c': 3}
print(diccionario_inverso(dic))
