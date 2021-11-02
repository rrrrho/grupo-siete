def escribir_fichero(arch, dato, tipo):
    # recibe el nombre de un archivo, el dato (registro) a escribir y el tipo de escritura --> 'a' para agregar, 'w' para sobreescribir (borrar todo y escribir)
    # sobre-escribe un fichero o agrega contenido, depende el tipo especificado
    with open(arch, tipo) as fichero:
        fichero.write(dato + '\n')

def arch_matriz(arch):
    # recibe el nombre de un archivo
    # transforma un archivo txt en matriz --> cada registro es una fila, y separa elementos por el delimitador ';'
    matriz =[]
    with open(arch, 'r') as fichero:
        i = 0
        linea =fichero.readline().strip()
        while linea !='' and i < 4:
            matriz.append(linea.split(';'))
            linea =fichero.readline().strip()
            i += 1
    return matriz

def matriz_arch(arch, matriz):
    # recibe el nombre de un archivo y una matriz
    # escribe una matriz en un txt --> cada fila es un registro que separa sus items con el delimitador ';'
    with open(arch, 'w') as fichero:
        fichero.write('')
    with open(arch, 'a') as fichero:
        for reg in matriz:
            fichero.write(';'.join(reg)+'\n')

def mod_arch(arch, id, string):
    # recibe el nombre de un archivo, un identificador de registro (string) y el string por el cual se quiere reemplazar el registro (osea otro registro que va en su lugar)
    # escribe un archivo nuevo con el contenido original y la modificación realizada
    with open(arch, 'r') as fichero:
        with open('datos/mod.txt', 'a') as fichero_mod:
            for linea in fichero:
                if id in linea:
                    fichero_mod.write(string)
                else:
                    fichero_mod.write(linea)

def traer_reg(arch, id):
    # recibe el nombre de un archivo y un identificador (string) para distinguir un registro
    # trae un registro de un archivo --> supone que si existe en el txt el registro especificado
    encontrado = False
    with open(arch, 'r') as fichero:
        while encontrado != True:
            linea = fichero.readline()
            if id in linea:
                encontrado = True
    return linea

def paciente_diccionario(string):
    # recibe un string con items separados por el delimitador ';' (registro en str)
    # transforma un string de un registro de pacientes a diccionario
    lista = string.rstrip().split(';')
    obj = {
        'dni': lista[0],
        'nombre': lista[1],
        'edad': lista[2]
    }
    return obj

def turno_diccionario(string):
    # recibe un string con items separados por el delimitador ';' (registro en str)
    # transforma un string de un registro de turnos a diccionario
    lista = string.rstrip().split(';')
    obj = {
        'dni': lista[0],
        'mes': lista[1],
        'dia': lista[2],
        'horario': lista[3]
    }
    return obj

def dicc_reg(obj):
    # recibe un diccionario (obj)
    # transforma un diccionario a un formato string que pueda ser escrito en un archivo
    valores = obj.values()
    return ';'.join(valores) + '\n'

def arch_dnis(arch):
    # recibe el nombre de un archivo
    # genera una lista de DNIS a partir de los primeros ocho caracteres de cada registro de un txt
    lista = []
    with open(arch, 'r') as fichero:
        linea =fichero.readline().strip()
        while linea !='':
            lista.append(linea[:8])
            linea = fichero.readline().strip()
    return lista

def arch_dicc(arch):
    # recibe el nombre de un archivo
    # crea una lista de diccionarios a partir de un txt
    i = 0
    lista = []
    with open(arch, 'r') as fichero:
        linea = fichero.readline()
        while linea != '' and i < 51:
            lista.append(paciente_diccionario(linea))
            linea = fichero.readline()
            i += 1
    return lista



