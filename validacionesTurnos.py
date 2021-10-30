from funciones.arch_manipulacion import arch_dnis
from datetime import datetime

def valPaciente(dni,arch):
    #Verifica que un DNI este en el archivo especificado.
    listdni = arch_dnis(arch)
    print(listdni)
    flag = False
    encontrado = False
    cont=0
    while flag==False and cont!=len(listdni):
        if dni == listdni[cont][0]:
            encontrado = True
            flag == True
        cont+=1
    return encontrado

def valDNI(dni):
    #Verifica que el DNI sea válido
    if dni.isnumeric()==True and len(dni)==8:
        return True
    else:
        return False
    
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
            print(dia,diamax)
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
    
#def valTurno(data):

    
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
