userbase = "s" #Usuario y contraseñas creadas solamente para verificar el correcto funcionamiento
passbase = "s123"

#------------------------------------------------------Login-----------------------------------------------------------
def pedircuenta():
    user = input("Introducir usuario:")
    pas = input("Introducir contraseña:")
    return user,pas

def validarusuario(usuario, contraseña, usuariobase, passbase):
    cont = 1
    validación = True
    while validación == True:
        if usuario == usuariobase and contraseña == passbase:
            validación = False
            print("Iniciando sesión...\n" "...\n" "Sesión Iniciada!")
        elif cont == 3:
            validación = False
            print("Se intentó el maximo numero de intentos, se ha bloqueado el inicio de sesión...")
        else:
            print("El usuario y contraseña no son validos")
            cont = cont + 1
            usuario,contraseña = pedircuenta()



user1,pas1 = pedircuenta()
validarusuario(user1,pas1, userbase, passbase)