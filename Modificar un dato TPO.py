import os; clear = lambda: os.system('cls'); clear(); import random;

#Funcion modificar
def modificar(lista_pacientes):
  dni = int(input("Ingrese el numero de DNI de la persona: "))
  persona.append(str(dni))
  nombre = input("Ingrese el nombre de la persona: ")
  persona.append(nombre.capitalize())
  edad = int(input("Ingrese la de la persona: "))
  persona.append(str(edad))
  if persona in lista_pacientes:
    x = lista_pacientes.index(persona)
    dato = input("Que dato desea modificar? (Dni, Nombre, Edad?): ")
    dato = dato.capitalize()
    if dato == "Dni":
      pregunta = int(input("Ingrese el nuevo numero de DNI: "))
      persona[0] = pregunta
      lista_pacientes[x] = persona
      print(lista_pacientes)
      ad = input("Desea modificar un dato mas? (yes, no): ")
      if ad == "yes":
        persona == []
        modificar(lista_pacientes)
      elif ad == "no":
        return lista_pacientes
    elif dato == "Nombre":
      pregunta = input("Ingrese el nuevo nombre: ")
      persona[1] = pregunta.capitalize()
      lista_pacientes[x] = persona
      print(lista_pacientes)
      ad = input("Desea modificar un dato mas? (yes, no): ")
      if ad == "yes":
        persona == []
        modificar(lista_pacientes)
      elif ad == "no":
        return lista_pacientes
    elif dato == "Edad":
      pregunta = int(input("Ingrese la nueva edad: "))
      persona[2] = pregunta
      lista_pacientes[x] = persona
      print(lista_pacientes)
      ad = input("Desea modificar un dato mas? (yes, no): ")
      if ad == "yes":
        persona == []
        modificar(lista_pacientes)
      elif ad == "no":
        return lista_pacientes
      else:
        print("Opcion incorrecta, porfavor vuelva a ingresar el DNI de la persona")
        modificar(lista_pacientes)
    else:
      print("Opcion incorrecta, porfavor repita los pasos otra ves")
      modificar(lista_pacientes)
  elif dni not in lista_pacientes:
      print("El numero de DNI no se encunetra registrado en nuestra base de datos")
      modificar(lista_pacientes)

#PP
paciente = [ ["46623410", "Martin", "45"] , ["25820887", "Jose", "64"] ]
persona = []
print(paciente)
modificar(paciente)