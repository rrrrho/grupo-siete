from funciones.arch_manipulacion import arch_dnis, traer_reg, turno_diccionario
from funciones.validaciones import validacion_dni

def modificar_turno():
    pacientes = arch_dnis('datos/turnos.txt')
    msj = 'Ingrese el DNI registrado en el turno: '
    while True:
        try:
            dni = int(input(msj))
            if not validacion_dni(dni):
                msj = 'Re-ingrese el DNI registrado en el turno: '
                continue
            break
        except:
            print('Por favor escriba un DNI válido.')
            msj = 'Re-ingrese el DNI registrado en el turno: '
    if str(dni) in pacientes:
        turno = turno_diccionario(traer_reg('datos/turnos.txt', str(dni)))       
        while True:
            try:
                opcion = int(input('¿Qué desea modificar? (1- Mes | 2- Día | 3- Horario: '))
                assert opcion == 1 or opcion == 2 or opcion == 3
                break
            except:
                print('Por favor escriba una opción válida.')
        if opcion == 1:
            mes_nuevo = input('Ingrese el nuevo mes: ')
            

