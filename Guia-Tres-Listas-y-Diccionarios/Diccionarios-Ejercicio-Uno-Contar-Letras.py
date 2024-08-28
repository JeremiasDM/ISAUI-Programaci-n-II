"""""
1. Contar letras: Escribe una función que reciba una cadena y devuelva un diccionario
con la frecuencia de cada letra en la cadena.
"""""

def contar_letras(cadena):
    frecuencia = {}
    for letra in cadena:
        if letra.isalpha():
            frecuencia[letra] = frecuencia.get(letra, 0) + 1
    return frecuencia

cadena = "Erre con erre guitarra, erre con erre barril. Rápido ruedan las ruedas del ruidoso ferrocarril"
print(contar_letras(cadena))
