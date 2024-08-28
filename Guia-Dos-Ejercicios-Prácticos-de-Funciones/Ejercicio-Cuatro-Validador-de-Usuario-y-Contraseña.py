""""
Ejercicio 4
Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te
devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido
hacer login incremente este valor, validar con otra función la cantidad de intentos posibles en
3 oportunidades.
"""""

def Login(usuario, contrasena):
    return usuario == "usuario1" and contrasena == "asdasd"

intentos = 0
while intentos < 3:
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    if Login(usuario, contrasena):
        print("Login exitoso")
        break
    else:
        intentos += 1
        print(f"Login fallido. Intentos restantes: {3 - intentos}")
else:
    print("Has superado el número de intentos permitidos.")

        