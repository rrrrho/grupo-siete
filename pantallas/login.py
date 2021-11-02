from extra.ascii_decoracion import titulo_login as titulo_l

userbase = "s" #Usuario y contraseñas creadas solamente para verificar el correcto funcionamiento
passbase = "s123"
#------------------------------------------------------Login-----------------------------------------------------------
def pedircuenta():
    user = input("Introducir usuario: ")
    pas = input("Introducir contraseña: ")
    return user,pas

def validarusuario(usuario, contraseña, usuariobase, passbase):
    # verifica si el usuario puede ingresar al sistema; si todo bien ok va a ser True, sino false
    cont = 1
    validacion = True
    ok = True
    while validacion == True:
        if usuario == usuariobase and contraseña == passbase:
            validacion = False
            print("Iniciando sesión...\n" "...\n" "Sesión Iniciada!")
        elif cont == 3:
            validacion = False
            ok = False
            print("Se intentó el maximo numero de intentos, se ha bloqueado el inicio de sesión...")
        else:
            print("El usuario y contraseña no son validos")
            cont = cont + 1
            usuario,contraseña = pedircuenta()
    return ok

def login():
    print(titulo_l)
    user1,pas1 = pedircuenta()
    return validarusuario(user1,pas1, userbase, passbase)