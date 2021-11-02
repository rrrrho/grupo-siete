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
def filtrarLineas(arch,criterio1,criterio2):
    listaelem= []
    with open(arch,'r') as file:
        linea = file.readline().strip()
        while linea !='':
            if criterio1 in linea:
                listafiltrada = linea.split(';')
                if criterio2 in listafiltrada:
                    listaelem.append(listafiltrada[-1])
            linea = file.readline().strip()
    return listaelem
    