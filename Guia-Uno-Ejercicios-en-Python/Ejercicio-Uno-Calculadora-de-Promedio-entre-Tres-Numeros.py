"""""
Ejercicio 1: Calculadora de Promedio
Escribe un programa en Python que solicite al usuario que ingrese tres números y luego calcule y muestre el promedio de esos números.
"""""

PrimerNumero = float(input("Ingrese el Primer Numero: "))
SegundoNumero = float(input("Ingrese el Segundo Numero: "))
TercerNumero = float(input("Ingrese el Tercer Numero: "))

Promedio = (PrimerNumero+SegundoNumero+TercerNumero) / 3

print("El Promedio de", PrimerNumero, SegundoNumero, "y", TercerNumero, "es", Promedio)