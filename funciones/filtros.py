def mayores_a(lista_dicc, edad):
    # recibe una lista de diccionarios con clave 'edad' y filtra la misma de acuerdo a si su valor es mayor al especificado en el segundo parámetro
    filtrado = []
    for dicc in lista_dicc:
        if int(dicc['edad']) > edad:
            filtrado.append(dicc)
    return filtrado