"""""
Ejercicio 8: Generador de Contraseñas Aleatorias 
Escribe un programa en Python que genere una contraseña aleatoria para el usuario. La contraseña debe tener una longitud de al menos 12 caracteres y debe contener una combinación de letras (mayúsculas y minúsculas), números y caracteres especiales. El programa debe mostrar la contraseña generada al usuario.
"""""

import random
import string

def generar_contrasena(longitud = 12):
    caracters = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracters) for _ in range(longitud))
    return contrasena

longitud_deseada = int(input("Porfavor indique cuantos caracteres debe tener la Contraseña:"))
nueva_contraseña = generar_contrasena(longitud_deseada)
print(f"Esta es su nueva contraseña: {nueva_contraseña}")


def run():

    generar_contrasena()
    