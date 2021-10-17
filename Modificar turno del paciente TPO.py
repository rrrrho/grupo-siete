import os; clear = lambda: os.system('cls'); clear(); import random;


#Funcion Modificar turno
def modificar_turno(lista_turnos):
  dni = int(input("Ingrese el nuermo de DNI de la persona a modificar el turno: "))
  for i in range(len(lista_turnos)):
    if str(dni) in lista_turnos[i][0]:
      pregunta = int(input("Que dato desea modificar? 1- Mes | 2- Dia | 3- Hora: "))
      if str(pregunta) == "1":
        dato = input("Ingrese el mes al cual quieras modificar el turno: ")
        lista_turnos[i][1] = dato
        print(lista_turnos)
        validacion = input("Desea modificar un dato mas? (yes, no): ")
        if validacion ==  "yes":
          modificar_turno(lista_turnos)
        elif validacion == "no":
          return lista_turnos
      elif str(pregunta) == "2":
        dato = int(input("Ingrese el dia al cual quieras modificar tu turno: "))
        lista_turnos[i][2] = dato
        print(lista_turnos)
        validacion = input("Desea modificar un dato mas? (yes, no): ")
        if validacion ==  "yes":
          modificar_turno(lista_turnos)
        elif validacion == "no":
          return lista_turnos
      elif str(pregunta) == "3":
        dato = input("Ingrese el horario al cual deseas modificar el turno [horas:minutos]: ")
        lista_turnos[i][3] = dato
        print(lista_turnos)
        validacion = input("Desea modificar un dato mas? (yes, no): ")
        if validacion ==  "yes":
          modificar_turno(lista_turnos)
        elif validacion == "no":
          return lista_turnos
      else:
        print("Opcion incorrecta")
        modificar_turno(lista_turnos)

#PP
turnos = [ ["46623410", "Enero", "22", "10:45"] , ["25820887", "Marzo", "31", "14:30"] ]
print(turnos)
modificar_turno(turnos)