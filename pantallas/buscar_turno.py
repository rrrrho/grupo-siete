def ingreso_y_validacion_dni():
    '''
    Pre: Pide DNI y lo valida
    Pos: Devuelve el DNI validado
    '''
    try:
        dni= input('Ingresar numero de DNI (Ingresar "no" para finalizar la busqueda de turnos): ')
        dni = dni.lower()
        if dni == 'no':
            pass
        else:
            verificacion = dni.isnumeric()
            assert (verificacion == True), 'Error, el DNI no debe contener letras y/o caracteres especiales...'
            assert (len(dni) == 8 or len(dni) == 7), 'Error, el DNI debe contener solamente 8 (ocho) numeros...'
    except AssertionError as error:
        print(error)
        return False
    else:
        return dni

def buscar_dni_en_archivo(dni):
    '''
    Pre: Ingresa el dni y busca la linea de datos de este mismo
    Pos: Retorna los datos de la linea del mismo dni ingresado, si no lo encuentra retorna falso
    '''
    datos = False
    arch= open('datos/turnos.txt','r')
    linea = arch.readline()
    while linea != '':
        if linea[:8] == dni:
            linea= linea.rstrip()
            datos= linea.split(';')
        linea = arch.readline()
    return datos
    arch.close()

def buscar_dni_en_archivo_v2(dni): #Lo mismo que el de arriba pero con iteración for
    datos= False
    with open('datos/turnos.txt','r') as file:
        for linea in file:
            if dni == linea[:8]:
                linea= linea.rstrip()
                datos= linea.split(';')
                dni,mes,dia,hora= tuple(datos)
    return datos

def mostrar_turno_dni():
    while True:
        try:
            dni= ingreso_y_validacion_dni()
            while dni != 'no':
                if dni != False:
                    dato = buscar_dni_en_archivo_v2(dni)
                    if dato != False:
                        dni,mes,dia,hora= dato
                        print(f'La persona de DNI nro: {dni}, tiene turno el {dia} de {mes} a las {hora}')
                    else:
                        print('No se encontró el numero de DNI...')
                dni= ingreso_y_validacion_dni()
            print('Finalizando...')
            break
        except FileNotFoundError:
            print('Error, archivo de datos no encontrado...')

def __main__():
    mostrar_turno_dni()

if __name__ == '__main__':
    __main__()