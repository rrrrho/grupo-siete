def mayores_a(matriz, edad):
    filtrado = []
    for fila in matriz:
        if fila[2] > edad:
            filtrado.append(fila)
    return filtrado