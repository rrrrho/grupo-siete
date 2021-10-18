import os; clear = lambda: os.system('cls'); clear(); import random;

#Funcion Eliminar turno
def eliminar_turno(lista_turnos):
  dni = int(input("Ingrese el numero de Dni del paciente: "))
  for i in range(len(lista_turnos)):
    if str(dni) in lista_turnos[i][0]:
      lista_turnos.pop(i)
      print(lista_turnos)
      validacion = input("Desea eliminar algun turno mas? (yes|no): ")
      if validacion == "yes":
        eliminar_turno(lista_turnos)
      elif validacion == "no":
        print("Volviendo al paso anterior.")
        return lista_turnos
      else:
        print("opcion incorrecta, volviendo al paso anterior.")
        return lista_turnos


#PP
turnos = [ ["46623410", "Marzo", "5", "13:30"], 
["25820887", "Agosto", "27", "9:30"], 
["12345678", "Enero", "14", "14:45"] ]
print(turnos)
eliminar_turno(turnos)