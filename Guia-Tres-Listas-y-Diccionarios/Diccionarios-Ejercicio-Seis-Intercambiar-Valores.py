"""""
6. Intercambiar valores: Crea una función que tome un diccionario y dos claves, e
intercambie los valores de esas dos claves en el diccionario.
"""""

def intercambiar_valores(dic, clave1, clave2):
    if clave1 in dic and clave2 in dic:
        dic[clave1], dic[clave2] = dic[clave2], dic[clave1]
    return dic

dic = {'a': 1, 'b': 2, 'c': 3}
print(intercambiar_valores(dic, 'a', 'c'))
