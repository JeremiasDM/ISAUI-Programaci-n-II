"""
Inventario de productos : Escribe una función que recibe un diccionario donde las claves son los nombres de los productos y los valores son listas de precios históricos de esos productos. 
La función debe devolver un nuevo diccionario donde las claves son los nombres de los productos y los valores son el precio promedio de cada producto.
"""

def calcular_promedios(estudiantes_notas):
    promedios = {}
    for estudiante, notas in estudiantes_notas.items():
        promedio = sum(notas) / len(notas)
        promedios[estudiante] = promedio
    return promedios

notas_estudiantes = {
    "Coca-Cola": [1,100,1000],
    "BloodBorn": [80,70,50],
    "X-Box series X": [550,9999999999,1]
}

promedios = calcular_promedios(notas_estudiantes)
print(promedios)