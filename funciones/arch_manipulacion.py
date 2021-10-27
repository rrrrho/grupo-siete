def escribir_fichero(arch, dato, tipo):
    # sobre-escribe un fichero o agrega contenido, depende el tipo especificado
    with open(arch, tipo) as fichero:
        fichero.write(dato + '\n')

def arch_matriz(arch):
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
    # escribe una matriz en un txt --> cada fila es un registro con el delimitador ';'
    with open(arch, 'w') as fichero:
        fichero.write('')
    with open(arch, 'a') as fichero:
        for reg in matriz:
            fichero.write(';'.join(reg)+'\n')

def mod_arch(arch, id, string):
    # escribe un archivo nuevo con el contenido original y la modificación realizada
    with open(arch, 'r') as fichero:
        with open('datos/mod.txt', 'a') as fichero_mod:
            for linea in fichero:
                if id in linea:
                    fichero_mod.write(string)
                else:
                    fichero_mod.write(linea)

def traer_reg(arch, id):
    # trae un registro de un archivo. supone que si existe el registro especificado
    encontrado = False
    with open(arch, 'r') as fichero:
        while encontrado != True:
            linea = fichero.readline()
            if id in linea:
                encontrado = True
    return linea

def reg_diccionario(string):
    # transforma un string de un registro de pacientes a diccionario
    lista = string.rstrip().split(';')
    obj = {
        'dni': lista[0],
        'nombre': lista[1],
        'edad': lista[2]
    }
    return obj

def dicc_reg(obj):
    # transforma un obj a un string que pueda ser escrito en un archivo
    valores = obj.values()
    return ';'.join(valores) + '\n'

def arch_dnis(arch):
    matriz = []
    with open(arch, 'r') as fichero:
        linea =fichero.readline().strip()
        while linea !='':
            matriz.append(linea.split(';')[0::3])
            linea = fichero.readline().strip()
    return matriz

def arch_dicc(arch):
    # crea una lista finita de diccionarios a partir de un txt
    i = 0
    lista = []
    with open(arch, 'r') as fichero:
        linea = fichero.readline()
        while linea != '' and i < 51:
            lista.append(reg_diccionario(linea))
            linea = fichero.readline()
            i += 1
    return lista




