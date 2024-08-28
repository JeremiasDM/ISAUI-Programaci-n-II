"""
Ejercicio 1
Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t
ú “. Crea un programa principal donde se use dicha función luego del ingreso del usuario.
"""

def ConvertirEspaciado(texto):
    return ' '.join(texto)

texto_usuario = input("Introduce un texto: ")
texto_espaciado = ConvertirEspaciado(texto_usuario)
print(texto_espaciado)
