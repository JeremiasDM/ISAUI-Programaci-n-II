"""""
7. Sumar valores: Escribe una función que reciba un diccionario con valores numéricos y
devuelva la suma de todos los valores.
"""""

def sumar_valores(dic):
    return sum(dic.values())

dic = {'a': 1, 'b': 2, 'c': 3}
print(sumar_valores(dic))
