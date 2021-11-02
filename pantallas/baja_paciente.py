import os; clear = lambda: os.system('cls'); clear()
from funciones.validaciones import validacion_dni, yes_no
from funciones.arch_manipulacion import mod_arch, arch_dnis

# La función de Ulises que la modifique para que funcione, hasta ahora intenté asegurarme de que no ocurra ningun error#Funcion
def baja_paciente():
    pacientes = arch_dnis('datos/pacientes.txt')
    msj = 'Ingrese número de DNI: '
    while True:
        try:
            dni = int(input(msj))
            if not validacion_dni(dni):
                raise Exception
            else:
                break
        except:
            print('Por favor escriba un DNI válido.')
            msj = 'Re-ingrese número de DNI: '

    if str(dni) in pacientes:
        mod_arch('datos/pacientes.txt', str(dni), '')
        os.remove('datos/pacientes.txt')
        os.rename('datos/mod.txt', 'datos/pacientes.txt')
        print('Paciente eliminado...')
    else:
        print('El DNI no se encuentra registrado en nuestro sistema.')

    seguir = input('¿Desea eliminar otro paciente? (yes, no): ').lower()
    while not yes_no(seguir):
        print('Por favor escriba yes o no.')
        seguir = input('¿Desea eliminar otro paciente? (yes, no): ').lower()
    if seguir == 'yes':
        baja_paciente()
