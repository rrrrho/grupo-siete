import os; clear = lambda: os.system('cls'); clear(); import random;

#funcion buscar dni
def arch_matriz(arch):
    with open(arch, 'r') as fichero:
        linea =fichero.readline().strip()
        while linea !='':
            matriz.append(linea.split(';')[0::3])
            linea = fichero.readline().strip()
    return matriz

matriz = []
filename = "datos/pacientes.txt"
arch_matriz(filename)
print(matriz)