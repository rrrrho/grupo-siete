import funciones.Colas as Colas
from funciones.validacionesTurnos import valMes, valDia
from funciones.valTurnoAux import filtrarLineas, filtrarMatriz    

def ordenarListasAColas(lista1,lista2):
    cola1ord= Colas.inicializar_cola()
    cola2ord= Colas.inicializar_cola()
    rango = len(lista2)
    for i in range(rango):
        minelem = min(lista2)
        minindice = lista2.index(minelem)
        dato2 = lista2.pop(minindice)
        dato1 = lista1.pop(minindice)
        Colas.acolar(cola1ord, dato1)
        Colas.acolar(cola2ord, dato2)
    lista1 += cola1ord
    lista2 += cola2ord
    
def informeColasTurnos(cola1,cola2,mes,dia):
    print(f'Turnos programados para el {dia} de {mes.title()}')
    while Colas.cola_vacia(cola1)==False:
        hora = Colas.primero(cola2)
        dni = Colas.primero(cola1)
        print(f'Paciente del DNI: {dni}, programado a las {hora}')
        Colas.desacolar(cola2)
        Colas.desacolar(cola1)
    
def listarTurnos(arch='datos/turnos.txt'):
    try:
        mesTurno = input("Ingresar Mes de turno: ")
        while valMes(mesTurno) == False:
            mesTurno = input("Ingresar un Mes válido para el turno: ")
            
        diaTurno = input("Ingresar Día del turno: ").title()
        while valDia(diaTurno, mesTurno.title())==False:
            diaTurno= input("Ingresar un número de día válido para el mes ingresado: ")
            
        matrizTurnos = filtrarLineas(arch, mesTurno.title())
        listaDNI = filtrarMatriz(matrizTurnos, diaTurno, 0)
        listaHora = filtrarMatriz(matrizTurnos, diaTurno, -1)
        if len(listaDNI)==0:
            print(f'No hay turnos programados para el {diaTurno} de {mesTurno}')
        else:
            ordenarListasAColas(listaDNI, listaHora)
            informeColasTurnos(listaDNI,listaHora,mesTurno,diaTurno)
    except:
        print("Error desconocido")
        raise
    finally:
        aea = input("Apretar 'Enter' para continuar al Menú Principal")
