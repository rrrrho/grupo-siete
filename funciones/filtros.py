def mayores_a(lista_dicc, edad):
    filtrado = []
    for dicc in lista_dicc:
        if int(dicc['edad']) > edad:
            filtrado.append(dicc)
    return filtrado