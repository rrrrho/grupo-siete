from os import rename, remove
from funciones.validaciones import validacion_dni, yes_no
from funciones.arch_manipulacion import mod_arch, arch_dnis

def baja_paciente():
    # elimina un registro en particulas del archivo 'pacientes.txt'
    pacientes = arch_dnis('datos/pacientes.txt')
    turnos = arch_dnis('datos/turnos.txt')
    msj = 'Ingrese número de DNI: '
    while True:
        try:
            dni = int(input(msj))
            if validacion_dni(dni):
                break
        except:
            print('Por favor escriba un DNI válido.')
        msj = 'Re-ingrese número de DNI: '

    if str(dni) in pacientes:
        mod_arch('datos/pacientes.txt', str(dni), '')
        remove('datos/pacientes.txt')
        rename('datos/mod.txt', 'datos/pacientes.txt')
        if str(dni) in turnos:
            mod_arch('datos/turnos.txt', str(dni), '')
            remove('datos/turnos.txt')
            rename('datos/mod.txt', 'datos/turnos.txt')
        print()
        print('Paciente eliminado con éxito.')

    else:
        print('El DNI no se encuentra registrado en nuestro sistema.')

    print()
    seguir = input('¿Desea eliminar a otro paciente? (yes, no): ').lower()
    while not yes_no(seguir):
        print('Por favor escriba yes o no.')
        seguir = input('¿Desea eliminar a otro paciente? (yes, no): ').lower()
    if seguir == 'yes':
        print()
        baja_paciente()
