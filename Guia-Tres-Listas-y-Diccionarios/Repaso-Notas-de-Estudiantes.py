"""
1. Notas de estudiantes : Escribe una función que recibe un diccionario donde las claves son nombres de estudiantes y los valores son listas de sus calificaciones. 
La función debe devolver un nuevo diccionario con las mismas claves pero donde los valores son la calificación promedio de cada estudiante.
"""

def calcular_promedios(estudiantes_notas):
    promedios = {}
    for estudiante, notas in estudiantes_notas.items():
        promedio = sum(notas) / len(notas)
        promedios[estudiante] = promedio
    return promedios

notas_estudiantes = {
    "Juan": [85, 90, 78],
    "María": [92, 88, 84],
    "Pedro": [70, 75, 80]
}

promedios = calcular_promedios(notas_estudiantes)
print(promedios)

