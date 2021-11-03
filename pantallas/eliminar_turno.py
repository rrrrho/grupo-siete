from funciones.arch_manipulacion import arch_dnis
from funciones.validaciones import validacion_dni, yes_no
from funciones.arch_manipulacion import mod_arch
import os; clear = lambda: os.system('cls')

def pedir_dni(msj):
    err = False
    while True:
        try:
            dni = int(input(msj))
            if validacion_dni(dni):
                break
        except:
            print('Por favor escriba un DNI válido.')
        if not err:
            msj = 'Re-'+msj.lower()
            err = True
    return dni

def seguir(msj, funcion):
    # recibe un mensaje personalizado para notificar al usuario si desea continuar, y un callback (función x para aplicar la recursividad)
    seguir = input(msj).lower()
    while not yes_no(seguir):
        print('Por favor escriba yes o no.')
        seguir = input(msj).lower()
    if seguir == 'yes':
        print()
        funcion()

def mod_eliminar_t():
    dni = pedir_dni('Ingrese el DNI registrado en el turno: ')
    eliminar_turno(dni)
    print()
    seguir('¿Desea eliminar otro turno? (yes, no): ', mod_eliminar_t)

def eliminar_turno(dni):
    # recibe un DNI para identificar el registro
    # elimina un registro del archivo 'turnos.txt'
    turnos = arch_dnis('datos/turnos.txt')
    if str(dni) in turnos:
        mod_arch('datos/turnos.txt', str(dni), '')
        os.remove('datos/turnos.txt')
        os.rename('datos/mod.txt', 'datos/turnos.txt')
        print('\nEl turno asociado ha sido eliminado con éxito.')
    else:
        print('\nNingún turno se encuentra registrado bajo ese DNI.')
 
    