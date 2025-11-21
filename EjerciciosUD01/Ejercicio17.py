# Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
# contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
# incorrecto

usuario_bd = "admin"
contrasena_bd = "1234"

usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

if usuario == usuario_bd:
    if contrasena == contrasena_bd:
        print("Inicio de sesión correcto")
    else:
        print("Contraseña incorrecta")
else:
    print("Nombre de usuario incorrecto")