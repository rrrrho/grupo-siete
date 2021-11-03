from funciones.arch_manipulacion import arch_dnis
from datetime import datetime
from funciones.valTurnoAux import OperacionHorario, convertirHora, filtrarLineas, filtrarMatriz

def valTurno(mes,dia,hora, arch='datos/turnos.txt'):
    matrizHorarios = filtrarLineas(arch,mes)
    listaHorarios = filtrarMatriz(matrizHorarios, dia, -1)
    listaHorarios.append(hora)
    listaHorarios.sort()          #Horarios ordenados de turnos correspondientes al mes y dia especificados
    horaConv = convertirHora(hora)
    
    if len(listaHorarios) == 1:                                 #El horario a verificar es el unico del día. Es válido
        return True
    elif listaHorarios.count(hora)>1:                           #El horario a verificar ya existe. Es inválido
        print("El horario ya existe!")
        return False
    indice = listaHorarios.index(hora)
    if listaHorarios[-1] != hora:                               #El horario a verificar no es el último. Hay uno más tarde que no debe interrumpirlo
        horariocomparar = convertirHora(listaHorarios[indice+1])
        nuevHoraC = OperacionHorario(horariocomparar, -15)
        if (horaConv > nuevHoraC) == True:
            print(f'El horario interrumpe al turno de las {listaHorarios[indice+1]} horas!')
            return False
    if listaHorarios[0] != hora:
        horariocomparar = convertirHora(listaHorarios[indice-1])
        nuevHoraC = OperacionHorario(horariocomparar, 15)
        if (horaConv < nuevHoraC) == True:
            print(f'El horario interrumpe al turno de las {listaHorarios[indice-1]} horas!')
            return False
    return True

def valDNI(dni):
    #Verifica que el DNI sea válido
    if dni.isnumeric()==True and (len(dni)==8 or len(dni)==7):
        return True
    else:
        return False

def valPaciente(dni,arch):
    #Verifica que un DNI este en el archivo especificado.
    listdni = arch_dnis(arch)
    flag = False
    encontrado = False
    cont=0
    while encontrado==False and cont!=len(listdni):
        if dni == listdni[cont]:
            encontrado = True
            flag == True
        cont+=1
    return encontrado

def valMes(mescadena):
    #Verifica que la string correspondiente a un Mes sea válida
    listames = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
    mescadena = mescadena.title()
    if mescadena.title() in listames:
        return True
    else:
        return False

def valDia(dia,mes):
    #Verifica que la string correspondiente a un Día exista en el Mes especificado
    try:
        dia = int(dia)
        lista31= ("Enero","Marzo","Mayo","Junio","Julio","Agosto","Octubre","Diciembre")
        if mes=="Febrero":
            if aniobisiesto()==True:
                diamax = 29
            else:
                diamax = 28
        elif mes in lista31:
            diamax = 31
        else:
            diamax = 30
        if 1<=dia<=diamax:
            return True
        else:
            return False
    except:
        return False

def valHora(hora):
    #Verifica que la string correspondiente a la Hora tenga un formato válido
    listahora = hora.split(':')
    horasola = hora.replace(":","")
    if len(listahora)==2 and horasola.isnumeric()==True:
        num1, num2 = listahora
        num1 = int(num1)
        num2 = int(num2)
        if 0<=num1<24 and 0<=num2<=59:
            return True
        else:
            return False
    else:
        return False

def aniobisiesto():
    #Averigua si el año actual es bisiesto
    anio = int(datetime.today().year)
    bisiesto = False
    if anio%4==0:
        if anio%100==0:
            if anio%400==0:
                bisiesto = True
        else:
            bisiesto = True
    return bisiesto
