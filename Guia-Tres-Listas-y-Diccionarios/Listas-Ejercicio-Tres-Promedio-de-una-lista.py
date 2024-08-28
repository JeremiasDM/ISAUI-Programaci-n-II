"""
Consigna 3 listas:
Los estudiantes deberán crear una función que reciba una lista de calificaciones, calcule la sumatoria de las notas, el promedio y determine la condición del alumno basado en el promedio. 
Si el promedio es mayor a 8, el alumno será considerado "PROMOCIONAL" caso contrario “REGULAR”.
"""

def evaluar_calificaciones(calificaciones):

    sumatoria = sum(calificaciones)
    
    promedio = sumatoria / len(calificaciones)
    
    if promedio > 8:
        condicion = "PROMOCIONAL"
    else:
        condicion = "REGULAR"
    
    return sumatoria, promedio, condicion


Calificasiones = input("Ingrese las Calificasiones:")

lista = [Calificasiones]

sumatoria, promedio, condicion = evaluar_calificaciones(Calificasiones)
print(f"Sumatoria: {sumatoria}")
print(f"Promedio: {promedio}")
print(f"Condición: {condicion}")
