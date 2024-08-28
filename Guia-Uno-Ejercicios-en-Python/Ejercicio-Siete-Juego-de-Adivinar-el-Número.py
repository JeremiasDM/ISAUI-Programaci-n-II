"""""
Ejercicio 7: Juego de Adivinar el Número 
Desarrolla un juego en el que el programa selecciona aleatoriamente un número entre 1 y 100 y el jugador debe adivinarlo. El programa debe proporcionar pistas al jugador si el número ingresado es demasiado alto o demasiado bajo. El juego debe continuar hasta que el jugador adivine correctamente el número.
"""""

import random

def Adivina_el_Numero():
    nombre = input("Bienvenido porfavor Ingrese su nombre:")
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinados = False
    while not adivinados:
        try:
            adivinanza = int(input("Ingrese un Numero entre 1 y 100:"))
            intentos += 1
            if adivinanza < numero_secreto:
                print("El Numero es demasiado bajo! Prueba con uno mas Alto")
            elif adivinanza > numero_secreto:
                print("El Numero es demasiado alto! Prueba con uno mas Bajo")
            else:
                adivinados = True
        except ValueError:
            print("Por favor ingrese un numero Entero")

    print(f"Felicitaciones {nombre} ! Adivinaste el numero en tan solo {intentos} intentos. ")

Adivina_el_Numero()