from funciones.arch_manipulacion import arch_dnis
from funciones.validaciones import validacion_dni, yes_no
from funciones.arch_manipulacion import mod_arch
import os; clear = lambda: os.system('cls')

def eliminar_turno():
    # elimina un registro del archivo 'turnos.txt'
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
        mod_arch('datos/turnos.txt', str(dni), '')
        os.remove('datos/turnos.txt')
        os.rename('datos/mod.txt', 'datos/turnos.txt')
        print('El turno ha sido eliminado con éxito.')
    else:
        print('Ningún turno se encuentra registrado bajo ese DNI.')

    print()
    seguir = input('¿Desea eliminar otro turno? (yes, no): ').lower()
    while not yes_no(seguir):
        print('Por favor escriba yes o no.')
        seguir = input('¿Desea eliminar otro turno? (yes, no): ').lower()
    if seguir == 'yes':
        print()
        eliminar_turno()
    