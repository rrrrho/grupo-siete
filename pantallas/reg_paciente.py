from funciones.arch_manipulacion import escribir_fichero, arch_dnis
from funciones.validaciones import validacion_dni, validacion_menores, validacion_nombre, yes_no

def reg_paciente():
    # registra un paciente en el sistema --> actualiza pacientes.txt de la carpeta datos
    pacientes = arch_dnis('datos/pacientes.txt') # trae una lista de DNIS registrados
    nombre = input('Ingrese el nombre completo del paciente: ').strip()
    while not validacion_nombre(nombre):
        nombre = input('Re-ingrese el nombre completo del paciente: ').strip()
    msj = 'Ingrese la edad del paciente: '
    while True:
        try:
            edad = int(input(msj))
            assert edad > 0 and edad < 105
            break
        except:
            print('Por favor escriba una edad válida.')
        msj = 'Re-ingrese la edad del paciente: '    
    if not validacion_menores(edad):
        print('La clínica no acepta pacientes menores de edad. Anulando el alta.\n')         
    else:
        msj = 'Ingrese el DNI del paciente: '
        while True:
            try:
                dni = int(input(msj))
                if validacion_dni(dni):
                    break
            except ValueError:
                print('ERROR. El DNI debe ser un número entero. Sin caracteres alfabeticos ni especiales.')
            msj = 'Re-ingrese el DNI del paciente: '
        try:
            if str(dni) not in pacientes:
                escribir_fichero('datos/pacientes.txt', f'{dni};{nombre.title()};{edad}', 'a')
                print()
                print('El paciente ha sido registrado con éxito.')
            else:
                print('Ya se encuentra registrado un paciente con dicho DNI. Anulando el alta.')
        except FileNotFoundError:
            print('ERROR. El registro de pacientes no fue encontrado en el directorio actual.')
    print()
    registrar= input('¿Desea registrar a otro paciente? (yes, no): ').lower()
    while not yes_no(registrar):
        print('Por favor escriba yes o no.')
        registrar= input('¿Desea registrar a otro paciente? (yes, no): ').lower()
    if registrar == 'yes':
        print()
        reg_paciente()
