from Producto import Producto #Importamos la clase Producto desde el archivo Producto.py.

class Alimento(Producto): #Definimos la clase Alimento, que hereda de Producto y representa un producto alimenticio.
    def __init__(self, nombre, precio, cantidad, fecha_expiracion): # Constructor de la clase Alimento, inicializa los atributos heredados y el específico (fecha_expiracion).

        super().__init__(nombre, precio, cantidad)  #Llama al constructor de la clase Producto para inicializar los atributos heredados.
        self.fecha_expiracion = fecha_expiracion  #Atributo que almacena la fecha de expiración del producto alimenticio.

    def mostrar_informacion(self): # Método para mostrar la información específica del producto alimenticio.

        info_producto = super().mostrar_informacion()  #Llama al método mostrar_informacion de la clase Producto.
        return f"{info_producto}, Fecha de Expiración: {self.fecha_expiracion}"  #Devuelve un string con la información completa del producto alimenticio.
