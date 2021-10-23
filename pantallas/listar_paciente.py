from funciones.arch_manipulacion import arch_matriz
from funciones.filtros import mayores_a
from funciones.validaciones import yes_no
from extra.ascii_decoracion import titulo_listar_p
import os; clear = lambda: os.system('cls')

def listar_p():
    # lista pacientes de pacientes.txt de la carpeta datos
    print(titulo_listar_p)
    msj = '''
¿Cómo desea listar los pacientes?

1. Por nombre
2. Por edad
3. Mayores a cierta edad

Escriba su opción: '''
    matriz_pacientes = arch_matriz('datos/pacientes.txt')
    while True:
        try:
            condicion = int(input(msj))
            assert condicion == 1 or condicion == 2 or condicion == 3
            break
        except:
            print('Por favor elija una opción válida.')
        msj = 'Escriba su opción: '
    if condicion == 1:
        matriz_pacientes.sort(key= lambda a: a[1])
    elif condicion == 2:
        matriz_pacientes.sort(key= lambda a: a[2])
    elif condicion == 3:
        while True:
            try:
                edad = int(input('Ingrese una edad: '))
                assert edad > 0 and edad < 105
                break
            except:
                print('Por favor escriba una edad válida.')
        matriz_pacientes = mayores_a(matriz_pacientes, str(edad))
        matriz_pacientes.sort(key= lambda a: a[2])
    print()
    for paciente in matriz_pacientes:
        print(f'Nombre: {paciente[1]}\nEdad: {paciente[2]}\nDNI: {paciente[0]}\n')

    seguir = input('¿Desea volver a filtrar? (yes, no): ').lower()
    while not yes_no(seguir):   
        print('ERROR. Por favor escriba yes o no.')
        seguir = input('¿Desea volver a filtrar? (yes, no): ').lower()
    if seguir == 'yes':
        clear()
        listar_p()


