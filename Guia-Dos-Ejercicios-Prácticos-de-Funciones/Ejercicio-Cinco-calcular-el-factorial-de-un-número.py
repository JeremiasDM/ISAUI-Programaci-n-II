"""""
Ejercicio 5
Crear una función recursiva que permita calcular el factorial de un número. Realiza un
programa principal donde se lea un número validado como entero, el cual es ingresado por
el usuario y se muestre el resultado del factorial.
"""""

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

numero = int(input("Introduce un número entero: "))
print(f"El factorial de {numero} es {factorial(numero)}")
