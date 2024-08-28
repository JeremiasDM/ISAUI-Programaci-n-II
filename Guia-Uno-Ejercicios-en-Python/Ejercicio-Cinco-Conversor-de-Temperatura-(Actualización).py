"""""
Ejercicio 5: Conversor de Temperatura (Actualización)
Mejora el programa de conversión de temperatura que escribiste anteriormente para que permita al usuario elegir entre convertir de grados Celsius a grados Fahrenheit o viceversa.
"""""

Temperatura = int(input("Ingrese un 1(UNO) si desea cambiar de Celsius a Fahrenheit, o un 2(DOS) de Fahrenheit a Celsius: "))

if Temperatura == 1:
    celsius = float (input("Ingrese la Temperatura en Grados Celsius: "))
    fahrenheit =  (celsius * 9/5) + 32
    print ("La Temperatura es Igual a ", fahrenheit, "° Fahrenheit")

if Temperatura == 2:
    fahrenheit = float(input("Ingrese la Temperatura en Grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print ("La Temperatura es Igual a ", celsius, "° Celsius")


