# registro de pacientes, faltan modificar muchas, agregar muchas, y mover muchas cosas :s

def validacion_nombre(nombre):
    if not nombre.isalpha():
        print('ERROR. El nombre debe tener solo caracteres alfabeticos.')
        return False
    return True

def validacion_menores(edad):
    if edad < 18:
        return False
    return True

def validacion_dni(dni):
    if len(str(dni)) != 8:
        print('ERROR. El DNI debe poseer únicamente ocho dígitos.')
        return False
    return True

pacientes = []

registrar = 'yes'
while registrar == 'yes':
    nombre = input('Ingrese el nombre del paciente: ').strip()
    while not validacion_nombre(nombre):
        nombre = input('Ingrese el nombre del paciente: ')
    print()
    while True:
        try:
            edad = int(input('Ingrese la edad del paciente: '))
            break
        except ValueError:
            print('ERROR. La edad debe ser un número entero. Sin caracteres alfabeticos ni especiales.')
    if not validacion_menores(edad):
        print('La clínica no acepta pacientes menores de edad. Anulando el alta.')
        registrar = input('¿Desea registrar a otro paciente? (yes, no): ')
        if registrar == 'no':
            break
        else:
            continue
    print()
    while True:
        try:
            dni = int(input('Ingrese el DNI del paciente: '))
            if not validacion_dni(dni):
                continue
            break 
        except ValueError:
            print('ERROR. El DNI debe ser un número entero. Sin caracteres alfabeticos ni especiales.')
    print()
    pacientes.append([dni, nombre.capitalize(), edad])
    print('Paciente registrado con éxito.')
    registrar = input('¿Desea registrar a otro paciente? (yes, no): ')

print(pacientes)