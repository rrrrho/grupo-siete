def validacion_nombre(nombre):
    # recibe un nombre --> verifica si no tiene caracteres númerico o especiales
    if not nombre.replace(' ', '').isalpha():
        print('ERROR. El nombre debe tener solo caracteres alfabeticos.')
        return False
    elif '' in nombre.split(' ') or len(nombre.split(' ')) == 1:
        print('ERROR. Asegurese de escribir nombre y apellido de manera correcta.')
        return False
    return True

def validacion_menores(edad):
    # recibe una edad en formato INT
    if edad < 18:
        return False
    return True

def validacion_dni(dni):
    # recibe un número de tipo INT sin puntos
    if len(str(dni)) != 8 and len(str(dni)) != 7:
        print('ERROR. El DNI debe poseer únicamente ocho o siete dígitos.')
        return False
    return True

def yes_no(dato):
    # recibe un string
    if dato.lower() != 'yes' and dato.lower() != 'no':
        return False
    return True

def es_mes(string):
    # recibe un string --> determina si es un mes válido
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    if string.capitalize() in meses:
        return True
    return False