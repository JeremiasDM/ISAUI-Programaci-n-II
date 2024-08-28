"""
Consigna 1 Combinado:
Los estudiantes deberán crear una función que filtre los datos del diccionario dicEstudiantes para incluir solo aquellos estudiantes que están inscritos en las carreras de "Software" y "Enfermería". 
La función debe recibir el diccionario dicEstudiantes y una lista  de carreras como parámetros, y devolver un nuevo diccionario con los estudiantes filtrados por : Software y Enfermería.
"""

diccEstudiantes = {
    'estudiante_1': {'nombre_y_apellido': 'Juan Pérez', 'dni': 12345678, 'sexo': 'Masculino', 'carrera': 'Turismo'},
    'estudiante_2': {'nombre_y_apellido': 'María López', 'dni': 23456789, 'sexo': 'Femenino', 'carrera': 'Software'},
    'estudiante_3': {'nombre_y_apellido': 'Carlos García', 'dni': 34567890, 'sexo': 'Masculino', 'carrera': 'Trekking'},
    'estudiante_4': {'nombre_y_apellido': 'Ana Fernández', 'dni': 45678901, 'sexo': 'Femenino', 'carrera': 'Espacios'},
    'estudiante_5': {'nombre_y_apellido': 'Luis Martínez', 'dni': 56789012, 'sexo': 'Masculino', 'carrera': 'Enfermería'},
    'estudiante_6': {'nombre_y_apellido': 'Sofía Gómez', 'dni': 67890123, 'sexo': 'Femenino', 'carrera': 'Turismo'},
    'estudiante_7': {'nombre_y_apellido': 'Pedro Rodríguez', 'dni': 78901234, 'sexo': 'Masculino', 'carrera': 'Software'},
    'estudiante_8': {'nombre_y_apellido': 'Elena Sánchez', 'dni': 89012345, 'sexo': 'Femenino', 'carrera': 'Trekking'},
    'estudiante_9': {'nombre_y_apellido': 'Miguel Torres', 'dni': 90123456, 'sexo': 'Masculino', 'carrera': 'Espacios'},
    'estudiante_10': {'nombre_y_apellido': 'Laura Ruiz', 'dni': 91234567, 'sexo': 'Femenino', 'carrera': 'Enfermería'}
}

def filtrar_estudiantes(dic_estudiantes, carreras):
    estudiantes_filtrados = {}
    for key, value in dic_estudiantes.items():
        if value['carrera'] in carreras:
            estudiantes_filtrados[key] = value
    return estudiantes_filtrados

carreras_que_filtrar = ['Software', 'Enfermería']


estudiantes_filtrados = filtrar_estudiantes(diccEstudiantes, carreras_que_filtrar)


print(estudiantes_filtrados)