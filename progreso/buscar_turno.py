import os; clear = lambda: os.system('cls'); clear(); import random;

#Funcion buscar turno
def buscar(lista_turnos):
  dni = int(input("Ingrese el numero de DNI de la persona: "))
  valor = False
  for x in range(len(lista_turnos)):
    if str(dni) in lista_turnos[x]:
      print(f"El DNI: {lista_turnos[x][0]} tiene un turno programado el {lista_turnos[x][2]} de {lista_turnos[x][1]} a las {lista_turnos[x][3]}")
      valor = True
  if valor == False:
    print("El DNI ingresado no tenia programado un turno.")


#PP
turnos = [ 
["46623410", "Marzo", "Lunes 5", "13:30"], 
["25820887", "Agosto", "Viernes 27", "9:30"], 
["12345678", "Enero", "Miercoles 14", "14:45"] ]
buscar(turnos)
