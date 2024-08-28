"""""
Ejercicio 2: Conversor de Moneda
Desarrolla un programa en Python que convierta una cantidad de dinero de dólares estadounidenses a euros. El programa debe solicitar al usuario que ingrese la cantidad en dólares y luego mostrar la cantidad equivalente en euros, utilizando un tipo de cambio fijo.
"""""

Dolar = float(input("Ingrese una Cantidad en Dolares: "))
TipoDeCambio = 0.93
Euro = Dolar * TipoDeCambio

print(Dolar, "Dolares equivalen a:", Euro)