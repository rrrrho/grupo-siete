from genericpath import isfile
from os import remove, rename
from funciones.arch_manipulacion import arch_dnis, traer_reg, turno_diccionario, dicc_reg, mod_arch
from funciones.validaciones import validacion_dni, yes_no
from funciones.validacionesTurnos import valTurno, valDia, valHora, valMes

def modificar_turno():
    # modifica el archivo 'turnos.txt' en base a ciertas condiciones
    turnos = arch_dnis('datos/turnos.txt')
    msj = 'Ingrese el DNI registrado en el turno: '
    while True:
        try:
            dni = int(input(msj))
            if validacion_dni(dni):
                break
        except:
            print('Por favor escriba un DNI válido.')
        msj = 'Re-ingrese el DNI registrado en el turno: '
    if str(dni) in turnos:
        turno = turno_diccionario(traer_reg('datos/turnos.txt', str(dni))) # traigo el turno y lo convierto a diccionario      
        while True:
            try:
                opcion = int(input('¿Qué desea modificar? 1- Mes | 2- Día | 3- Horario: '))
                assert opcion == 1 or opcion == 2 or opcion == 3
                break
            except:
                print('Por favor escriba una opción válida.')
        if opcion == 1:
            print()
            msj = 'Ingrese el nuevo mes (Ejemplo: Febrero): '
            while True:
                try:
                    mes_nuevo = input(msj).strip()
                    assert valMes(mes_nuevo)
                    break
                except:
                    print('Por favor escriba un mes válido.')
                msj = 'Re-ingrese el nuevo mes: '
            if valTurno(mes_nuevo.capitalize(), turno['dia'], turno['horario']):
                turno['mes'] = mes_nuevo.capitalize()
                turno = dicc_reg(turno) # convierto el diccionario a formato string
                mod_arch('datos/turnos.txt', str(dni), turno)
                remove('datos/turnos.txt')
                rename('datos/mod.txt', 'datos/turnos.txt')
                print('El mes del turno ha sido modificado con éxito.')
        elif opcion == 2:
            print()
            msj = 'Ingrese el nuevo día: '
            while True:
                try:
                    dia_nuevo = int(input(msj))
                    assert dia_nuevo not in [1,8,15,22], "Se ingresó un día en el que el médico no trabaja."
                    if not valDia(dia_nuevo, turno['mes']):
                        raise Exception
                    break
                except AssertionError as err:
                    print(err)
                except:
                    print('Por favor escriba un día válido.')
                msj = 'Re-ingrese el nuevo día: '
            if valTurno(turno['mes'], str(dia_nuevo), turno['horario']):
                turno['dia'] = str(dia_nuevo)
                turno = dicc_reg(turno)
                mod_arch('datos/turnos.txt', str(dni), turno)
                remove('datos/turnos.txt')
                rename('datos/mod.txt', 'datos/turnos.txt')
                print('El día del turno ha sido modificado con éxito.')
        elif opcion == 3:
            print()
            msj = 'Ingrese el nuevo horario: '
            while True:
                try:
                    horario_nuevo = input(msj)
                    assert valHora(horario_nuevo), 'Por favor escriba un horario válido'
                    assert 1000 <= int(horario_nuevo.replace(":","")) <= 1400, 'Se ingresó un horario en el que el médico no trabaja.'
                    break
                except AssertionError as err:
                    print(err)
                msj = 'Re-ingrese el nuevo horario: '

            mod_arch('datos/turnos.txt', str(dni), '') 
            # necesito una version del txt donde no se encuentre el registro que quiero modificar -> se va a llamar 'mod.txt'. la función utiliza ese nombre
            if valTurno(turno['mes'], turno['dia'], horario_nuevo, 'datos/mod.txt'):
                turno['horario'] = horario_nuevo
                turno = dicc_reg(turno)
                remove('datos/mod.txt') 
                # tengo que borrar la version creada para poder sobreescribir el archivo original -> uso el mismo nombre de archivo para sobreescribir
                mod_arch('datos/turnos.txt', str(dni), turno)
                remove('datos/turnos.txt')
                rename('datos/mod.txt', 'datos/turnos.txt')
                print('El horario del turno ha sido modificado con éxito.')

            if isfile('datos/mod.txt'): 
                # en caso de que no haya entrado en el anterior if me aseguro de todas maneras de borrar 'mod.txt'
                remove('datos/mod.txt')
    else:
        print('No hay ningún turno registrado bajo ese DNI.')

    print()
    validacion = input("¿Quiere seguir modificando turnos? (yes | no): ").lower()
    while not yes_no(validacion):
        print('ERROR. Por favor elija una opción válida.')
        validacion = input("¿Quiere seguir modificando turnos? (yes | no): ").lower()   
    if validacion == "yes":
        print()
        modificar_turno()






            

