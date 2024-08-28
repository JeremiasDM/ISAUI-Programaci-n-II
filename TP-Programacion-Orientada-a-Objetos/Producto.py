class Producto:
    def __init__(self, nombre, precio, cantidad):
        
        self.nombre = nombre  # Atributo que almacena el nombre del producto.
        self.precio = precio  # Atributo que almacena el precio del producto.
        self.cantidad = cantidad  # Atributo que almacena la cantidad disponible del producto.

    def mostrar_informacion(self): #Método para mostrar la información del producto.
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}" #Devuelve un string con la información del producto.
