"""
Consigna 2 Diccionario: 
Los estudiantes deberán crear una función que modifique el diccionario dicEstudiantes eliminando la clave "sexo" y añadiendo una nueva clave "edad" con valores generados aleatoriamente
entre 18 y 32 años (inclusive) para cada estudiante.
"""

diccEstudiantes = {
    'estudiante_1': {'nombre_y_apellido': 'Juan Pérez', 'DNI': 12345678, 'sexo': 'Masculino', 'carrera': 'Turismo'},
    'estudiante_2': {'nombre_y_apellido': 'María López', 'DNI': 23456789, 'sexo': 'Femenino', 'carrera': 'Software'},
    'estudiante_3': {'nombre_y_apellido': 'Carlos García', 'DNI': 34567890, 'sexo': 'Masculino', 'carrera': 'Trekking'},
    'estudiante_4': {'nombre_y_apellido': 'Ana Fernández', 'DNI': 45678901, 'sexo': 'Femenino', 'carrera': 'Espacios'},
    'estudiante_5': {'nombre_y_apellido': 'Luis Martínez', 'DNI': 56789012, 'sexo': 'Masculino', 'carrera': 'Enfermería'},
    'estudiante_6': {'nombre_y_apellido': 'Sofía Gómez', 'DNI': 67890123, 'sexo': 'Femenino', 'carrera': 'Turismo'},
    'estudiante_7': {'nombre_y_apellido': 'Pedro Rodríguez', 'DNI': 78901234, 'sexo': 'Masculino', 'carrera': 'Software'},
    'estudiante_8': {'nombre_y_apellido': 'Elena Sánchez', 'DNI': 89012345, 'sexo': 'Femenino', 'carrera': 'Trekking'},
    'estudiante_9': {'nombre_y_apellido': 'Miguel Torres', 'DNI': 90123456, 'sexo': 'Masculino', 'carrera': 'Espacios'},
    'estudiante_10': {'nombre_y_apellido': 'Laura Ruiz', 'DNI': 91234567, 'sexo': 'Femenino', 'carrera': 'Enfermería'}
}

import random

def modificar_diccionario(dicEstudiantes):
    for estudiante in dicEstudiantes.values():
        
        if 'sexo' in estudiante:
            del estudiante['sexo']
        

        estudiante['edad'] = random.randint(18, 32)

modificar_diccionario(diccEstudiantes)

print(diccEstudiantes)
