from funciones.arch_manipulacion import arch_dnis
from funciones.validaciones import validacion_dni, yes_no
from funciones.arch_manipulacion import mod_arch
from os import remove, rename

def eliminar_turno():
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
        mod_arch('datos/turnos.txt', str(dni), '')
        remove('datos/turnos.txt')
        rename('datos/mod.txt', 'datos/turnos.txt')
    else:
        print('Ningún turno se encuentra registrado bajo ese DNI.')

    seguir = input('¿Desea eliminar otro turno? (yes, no): ').lower()
    while not yes_no(seguir):
        print('Por favor escriba yes o no.')
        seguir = input('¿Desea eliminar otro turno? (yes, no): ').lower()
    if seguir == 'yes':
        eliminar_turno()
    