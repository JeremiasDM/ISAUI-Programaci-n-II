"""""
Ejercicio 6
Suma de pares: Escribe una función que tome una lista de números y devuelva la suma de
los números pares en la lista.
"""""
def suma_pares(lista):
    return sum(x for x in lista if x % 2 == 0)

numeros = list(map(int, input("Introduce números separados por espacio: ").split()))
print(f"La suma de los números pares es: {suma_pares(numeros)}")


