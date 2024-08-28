"""""
Ejercicio 11: Adivinador de números
Crea un juego que le pida al usuario que piense un número entre 1 y 100. Luego, el programa debe intentar adivinar ese número utilizando la estrategia de búsqueda binaria. 
En cada intento, el programa debe preguntar al usuario si el número a adivinar es mayor, menor o igual al número propuesto por el programa. 
El juego debe terminar cuando el programa adivine el número correcto.
"""""

def adivinador_de_Numeros():
    Maximo = 100
    Minimo = 1
    intentos = 0
    
    while True:
        intentos += 1
        Numero_Adivinar = (Maximo + Minimo) // 2
        
        respuesta = input(f"El numero en el que pienso es {Numero_Adivinar}? Ingrese si el Numero propuesto es <(Menor), >(Mayor) o =(Igual) al propuesto: ")
        if respuesta == "=":
            print(f"Adiviné el numero en {intentos} intentos")
            break
        elif respuesta == ">":
            Maximo = Numero_Adivinar
        elif respuesta == "<":
            Minimo = Numero_Adivinar
        else:
            print("Ingrese una respuesta valida")

adivinador_de_Numeros()
            

