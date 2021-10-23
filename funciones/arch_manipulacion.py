def existe_fichero(arch, dato):
    # busca por cada línea un dato, si existe retorna True, sino False
    encontrado = False
    with open(arch, 'r') as fichero:
        linea = fichero.readline()
        while linea != '' and encontrado != True:
            if dato in linea:
                encontrado = True
            linea = fichero.readline()
    return encontrado

def escribir_fichero(arch, dato, tipo):
    # sobre-escribe un fichero o agrega contenido, depende el tipo especificado
    with open(arch, tipo) as fichero:
        fichero.write(dato + '\n')

def arch_matriz(arch):
    # transforma un archivo txt en matriz --> cada registro es una fila, y separa elementos por el delimitador ';'
    matriz =[]
    with open(arch, 'r') as fichero:
        linea =fichero.readline().strip()
        while linea !='':
            matriz.append(linea.split(';'))
            linea =fichero.readline().strip()
    return matriz

def matriz_arch(arch, matriz):
    # escribe una matriz en un txt --> cada fila es un registro con el delimitador ';'
    with open(arch, 'w') as fichero:
        fichero.write('')
    with open(arch, 'a') as fichero:
        for reg in matriz:
            fichero.write(';'.join(reg)+'\n')
