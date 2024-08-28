# Importamos las clases Electronico y Alimento desde sus respectivos archivos.
from Electronico import Electronico
from Alimento import Alimento

televisor = Electronico(nombre="Televisor", precio=400.00, cantidad=10, marca="Samsung", modelo="QLED123") #Crear una instancia de la clase Electronico con los atributos específicos.

manzanas = Alimento(nombre="Manzanas", precio=0.50, cantidad=10000, fecha_expiracion="2024-12-31") #Crear una instancia de la clase Alimento con los atributos específicos.

print(televisor.mostrar_informacion()) #Mostrar la información del producto electrónico llamando al método mostrar_informacion.

print(manzanas.mostrar_informacion()) #Mostrar la información del producto alimenticio llamando al método mostrar_informacion.
