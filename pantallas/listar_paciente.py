from funciones.arch_manipulacion import arch_dicc
from funciones.filtros import mayores_a
from funciones.validaciones import yes_no
import os; clear = lambda: os.system('cls')

def listar_p():
    # lista pacientes de pacientes.txt de la carpeta datos
    msj = '''
¿Cómo desea listar los pacientes?

1. Por nombre
2. Por edad
3. Mayores a cierta edad

Escriba su opción: '''
    pacientes = arch_dicc('datos/pacientes.txt')
    while True:
        try:
            condicion = int(input(msj))
            assert condicion == 1 or condicion == 2 or condicion == 3
            break
        except:
            print('Por favor elija una opción válida.')
        msj = 'Escriba su opción: '
    if condicion == 1:
        pacientes.sort(key= lambda a: a['nombre'])
    elif condicion == 2:
        pacientes.sort(key= lambda a: int(a['edad']))
    elif condicion == 3:
        while True:
            try:
                edad = int(input('Ingrese una edad: '))
                assert edad > 0 and edad < 105
                break
            except:
                print('Por favor escriba una edad válida.')
        pacientes = mayores_a(pacientes, edad)
        pacientes.sort(key= lambda a: int(a['edad']))
    print()
    for paciente in pacientes:
        print(f'Nombre: {paciente["nombre"]}\nEdad: {paciente["edad"]}\nDNI: {paciente["dni"]}\n')

    seguir = input('¿Desea volver a filtrar? (yes, no): ').lower()
    while not yes_no(seguir):   
        print('ERROR. Por favor escriba yes o no.')
        seguir = input('¿Desea volver a filtrar? (yes, no): ').lower()
    if seguir == 'yes':
        clear()
        listar_p()


