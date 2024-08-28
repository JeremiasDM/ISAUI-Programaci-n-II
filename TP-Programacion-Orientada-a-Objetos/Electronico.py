from Producto import Producto #Importamos la clase Producto desde el archivo Producto.py.

class Electronico(Producto): #Clase Electronico, que hereda de Producto y representa un producto electrónico.

    def __init__(self, nombre, precio, cantidad, marca, modelo): #Constructor de la clase Electronico, inicializa los atributos heredados y los específicos (marca y modelo).

        super().__init__(nombre, precio, cantidad)  # Llama al constructor de la clase Producto para inicializar los atributos heredados.
        self.marca = marca  #Atributo que almacena la marca del producto electrónico.
        self.modelo = modelo  #Atributo que almacena el modelo del producto electrónico.

    def mostrar_informacion(self): #Método para mostrar la información específica del producto electrónico.
        
        info_producto = super().mostrar_informacion()  #Llama al método mostrar_informacion de la clase Producto.
        return f"{info_producto}, Marca: {self.marca}, Modelo: {self.modelo}"  #Devuelve un string con la información completa del producto electrónico.
