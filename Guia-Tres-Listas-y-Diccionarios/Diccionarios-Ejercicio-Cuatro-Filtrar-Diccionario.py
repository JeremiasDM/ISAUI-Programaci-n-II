"""""
4. Filtrar diccionario: Escribe una función que reciba un diccionario y una lista de claves,
y devuelva un nuevo diccionario solo con las claves especificadas.
"""""

def filtrar_diccionario(dic, claves):
    return {clave: dic[clave] for clave in claves if clave in dic}

dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
claves = ['a', 'e']
print(filtrar_diccionario(dic, claves))