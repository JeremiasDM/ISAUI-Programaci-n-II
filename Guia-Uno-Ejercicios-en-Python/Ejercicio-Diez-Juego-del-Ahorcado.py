"""""
Ejercicio 10: Juego del Ahorcado 
Juego de Ahorcado: Crea un juego de ahorcado donde el jugador debe adivinar una palabra oculta antes de que se agoten los intentos. Puedes hacerlo con una lista predefinida de palabras.
"""""
import random

palabras = ['Python','Programacion','Base de Datos','Software','RAM','Algoritmo','CPU','']
secreta = random.choice(palabras)
cadena = "-"* len(secreta)
print("Bienvenido al Juego del Ahorcado")
intentos = 0

while intentos < 6:
    print(cadena)
    letra = input("Ingresa una letra: ")
    if letra in secreta:
        for i in range(len(secreta)):
            if secreta[i] == letra:
                cadena = cadena[:i] + letra + cadena[i+1:]
    else:
        if intentos == 0:
            print("O")
        elif intentos == 1:
            print("O")
            print("|")
        elif intentos == 2:
            print(" O")
            print("/|")
        elif intentos == 3:
            print(" O")
            print("/|\\")
        elif intentos == 4:
            print(" O")
            print("/|\\")
            print("/")
        elif intentos == 5:
            print(" O")
            print("/|\\")
            print("/ \\")
            print(f"Perdiste =( la Palabra era {secreta}")
            break
    
    if cadena == secreta:
        print(f"Felicidades lo lograste la palabra secreta era {secreta}")
        break
    intentos += 1
       
