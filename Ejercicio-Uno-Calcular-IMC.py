Nombre = input("Ingrese su Nombre: ")
Peso = float(input("Ingrese su Peso en Kilogramos: "))
Altura = float(input("Ingrese su Altura en Metros: "))

IMC = Peso / (Altura * Altura)

print("Hola", Nombre, "su Indice de Masa Corporal (IMC) es: ", IMC)
    
if IMC < 18.5:
    print("Usted está Bajo de Peso.")
elif IMC < 25:
    print("Su peso es Normal.")
elif IMC < 30:
    print("Usted tiene Sobrepeso.")
else:
    print("Usted es Obeso.")


