import os; clear = lambda: os.system('cls'); clear(); import random;

#Funcion buscar turno
def buscar(lista_turnos):
  dni = int(input("Ingrese el numero de DNI de la persona: "))
  valor = False
  for x in range(len(lista_turnos)):
    if str(dni) in lista_turnos[x]:
      print(lista_turnos[x])
      valor = True
  if valor == False:
    print("El DNI ingresado no tenia programado un turno.")


#PP
turnos = [ 
["46623410", "Marzo", "Lunes", "13:30"], 
["25820887", "Agosto", "Viernes", "9:30"], 
["12345678", "Enero", "Miercoles", "14:45"] ]
buscar(turnos)