import datetime

#Recibe un horario en formato time y un entero representando la cantidad de minutos a sumar(o restar si esta en negativo)
def OperacionHorario(horario,vminutos):
    AUX = datetime.date(1,1,1)
    Completa = datetime.datetime.combine(AUX, horario)
    TDELTA = datetime.timedelta(minutes=vminutos)
    NuevaFechaHora = Completa + TDELTA
    Result= NuevaFechaHora.time()
    return Result

#Convierte una formato de cadena representando a una hora(ej 12:30) en el formato time
def convertirHora(hora):
    horaform = hora.split(':')
    Horario1 = datetime.time(int(horaform[0]),int(horaform[1]))
    return Horario1

#Abre un archivo, y si se encuentra cierta cadena en un registro, lo extrae
def filtrarLineas(arch,criterio1):
    listaelem= []
    with open(arch,'r') as file:
        linea = file.readline().strip()
        while linea !='':
            if criterio1 in linea:
                listafiltrada = linea.split(';')
                listaelem.append(listafiltrada)
            linea = file.readline().strip()
    return listaelem

#Recibe una matriz, y si se encuentra cierto criterio en una lista, extrae un indice especifico
def filtrarMatriz(matriz, criterio, indice):
    lista= []
    for elem in matriz:
        if criterio in elem:
            lista.append(elem[indice])
    return lista
    