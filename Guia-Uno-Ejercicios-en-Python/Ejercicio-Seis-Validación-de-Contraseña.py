"""""
Ejercicio 6: Validación de Contraseña 
Escribe un programa en Python que valide una contraseña ingresada por el usuario. La contraseña debe cumplir con los siguientes requisitos:
-Debe tener al menos 8 caracteres de longitud.
-Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
-El programa debe informar al usuario si la contraseña es válida o no.
"""""

def Validador_Contrasena(Contrasena):
    if len(Contrasena) < 8:
        return False
    Contiene_Mayuscula = False
    Contiene_Minuscula = False
    Contiene_Numero = False
    Contiene_CaracterSpe = False
    for Caracter in Contrasena:
        if Caracter.isupper():
            Contiene_Mayuscula = True
        elif Caracter.islower():
            Contiene_Minuscula = True
        elif Caracter.isdigit():
            Contiene_Numero = True
        elif Caracter in "!@#$%^&*()_-+={}[]:;',<.>/?":
            Contiene_CaracterSpe = True
    return Contiene_Mayuscula and Contiene_Minuscula and Contiene_Numero and Contiene_CaracterSpe

def main():
    Contrasena = input("Ingrese una Contraseña que contenga Al Menos 8 digitos, un Numero, una letra MAYUSCULA y una minuscula y un Caracter Especial: ")
    if Validador_Contrasena(Contrasena):
        print("Su Contraseña es Valida")
    else:
        print("Su Contraseña no cumple con los requisitos minimos")

if __name__ == "__main__":
    main()



