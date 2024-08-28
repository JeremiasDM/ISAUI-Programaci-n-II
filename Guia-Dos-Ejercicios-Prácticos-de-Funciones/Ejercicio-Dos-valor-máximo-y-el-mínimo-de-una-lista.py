"""
Ejercicio 2
Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
máximo y el mínimo, utilizando la función anterior.
"""

def calcularMaxMin(lista):
    return max(lista), min(lista)

# Programa principal
numeros = list(map(float, input("Introduce números separados por espacio: ").split()))
maximo, minimo = calcularMaxMin(numeros)
print(f"El valor máximo es: {maximo}")
print(f"El valor mínimo es: {minimo}")
