import os; clear = lambda: os.system('cls'); clear(); import random;

#Funcion modificar
def modificar_dato(lista_pacientes):
  dni = int(input("Ingrese el numero de DNI de la persona: "))
  for i in range(len(lista_pacientes)):
    if str(dni) in lista_pacientes[i][0]:
      pregunta = int(input("Que desea modificar? 1- Dni | 2- Nombre | 3- Edad: "))
      if str(pregunta) == "1":
        dato = int(input("Ingrese el nuevo numero de DNI del paciente: "))
        lista_pacientes[i][0] = str(dato)
        print(lista_pacientes)
        validacion = input("Quiere modificar un dato mas? (yes | no): ")
        if validacion == "yes":
          modificar_dato(lista_pacientes)
        elif validacion == "no":
          return lista_pacientes
      elif str(pregunta) == "2":
        dato = input("Ingrese el nuevo nombre del paciente: ")
        lista_pacientes[i][1] = dato.capitalize()
        print(lista_pacientes)
        validacion = input("Quiere modificar un dato mas? (yes | no): ")
        if validacion == "yes":
          modificar_dato(lista_pacientes)
        elif validacion == "no":
          return lista_pacientes
      elif str(pregunta) == "3":
        dato = int(input("Ingrese la nueva edad del paciente: "))
        lista_pacientes[i][2] = dato
        print(lista_pacientes)
        validacion = input("Quiere modificar un dato mas? (yes | no): ")
        if validacion == "yes":
          modificar_dato(lista_pacientes)
        elif validacion == "no":
          return lista_pacientes
      else: 
        print("Opcion incorrecta, porfavor vuelva a ingresar otra vez el numero de DNI y siga los pasos")
        modificar_dato(lista_pacientes)

#PP
paciente = [ ["46623410", "Martin", "45"] , ["25820887", "Jose", "64"] ]
print(paciente)
modificar_dato(paciente)