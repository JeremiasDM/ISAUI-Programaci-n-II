"""""
Ejercicio 9: Calculadora de Factorial 
Desarrolla una calculadora que calcule el factorial de un número ingresado por el usuario. El factorial de un número entero positivo n se define como el producto de todos los enteros positivos menores o iguales a n. El programa debe manejar números enteros grandes y mostrar el resultado.
"""""

def calcular_factorial(numero):
  if numero < 0:
    return "No se puede calcular el factorial de un número negativo."
  elif numero == 0:
    return 1
  else:
    factorial = 1
    for i in range(1, numero + 1):
      factorial *= i
    return factorial

def main():
  while True:
    try:
      numero = int(input("Ingrese un número entero no negativo:"))
      if numero < 0:
        print("No se puede calcular el factorial de un número negativo.")
      else:
        break
    except ValueError:
      print("¡Entrada no válida! Ingrese un número entero.")

  resultado_factorial = calcular_factorial(numero)
  print(f"El factorial de {numero} es: {resultado_factorial}")

if __name__ == "__main__":
  main()

