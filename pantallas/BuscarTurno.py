def buscar_dni_en_archivo(dni):
    '''
    Pre: Ingresa el dni y busca la linea de datos de este mismo
    Pos: Retorna los datos de la linea del mismo dni ingresado, si no lo encuentra retorna falso
    '''
    datos = False
    arch= open('Datos/dato pacientes.txt','r')
    linea = arch.readline()
    while linea != '':
        if linea[:8] == dni:
            linea= linea.rstrip()
            datos= linea.split(';')
        linea = arch.readline()
    return datos
    arch.close()

def buscar_turno(): #Pide el dni, lo valida y muestra los datos retornados de 'buscar_dni_en_Archivo'
    while True:
        try:
            dni = input('Introducir numero del dni:')
            dni = dni.lower()
            while dni != 'no':
                verificacion = dni.isnumeric()
                assert (verificacion == True), 'Error, el DNI debe contener numeros solamente...'
                assert (len(dni) == 8), 'Error, el DNI debe contener solamente 8 (ocho) numeros...'
                dato= buscar_dni_en_archivo(dni)
                if dato != False:
                    dni,mes,dia,hora= dato
                    print(f'La persona de DNI nro: {dni} tiene turno el {dia} de {mes} a las {hora}')
                else:
                    print('No se encontró el DNI introducido...')
                dni = input('Introducir numero del dni(para terminar con la busqueda, introduzca "no"):')
                dni = dni.lower()
            break
        except AssertionError as error:
            print(error)

def __main__():
    buscar_turno()

if __name__ == '__main__':
    __main__()