"""""
9. Producto de elementos: Escribe una función que tome una lista de números y
devuelva el producto de todos los elementos.
"""""

def producto_elementos(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

numeros = [1, 2, 3, 4, 5]
print(producto_elementos(numeros))
