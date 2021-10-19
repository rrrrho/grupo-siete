import os; clear = lambda: os.system('cls'); clear(); import random;
from funciones.validaciones import validacion_dni, validacion_menores, validacion_nombre, yes_no

#Funcion modificar
def main():
  lista_pacientes = [["46623410", "Martin", "45"], ["25820887", "Jose", "64"]]
  # PEDIDO DE DATOS Y VALIDACIÓN/MANEJO DE ERRORES DE LOS MISMOS
  msj = "Ingrese el número de DNI de la persona: "
  while True:
    try:
      dni = int(input(msj))
      if validacion_dni(dni):
        break
    except ValueError:
      print('ERROR. El DNI debe ser un número entero. Sin caracteres alfabeticos ni especiales.')
    msj = "Re-ingrese el numero de DNI de la persona: "
  for i in range(len(lista_pacientes)):
    if str(dni) in lista_pacientes[i][0]:
      while True:
        try:
          pregunta = int(input("¿Qué desea modificar? 1- Dni | 2- Nombre | 3- Edad: "))
          assert pregunta == 1 or pregunta == 2 or pregunta == 3
          break
        except:
          print('ERROR. Por favor elija una opción válida.')
      if str(pregunta) == "1":
        msj = "Ingrese el nuevo número de DNI del paciente: "
        while True:
          try:
            dato = int(input(msj))
            if validacion_dni(dato):
              break
          except:
            print('ERROR. El DNI debe ser un número entero. Sin caracteres alfabeticos ni especiales.')
          msj = "Re-ingrese el nuevo número de DNI del paciente: "
        lista_pacientes[i][0] = str(dato)
      elif str(pregunta) == "2":
        msj = "Ingrese el nuevo nombre del paciente: "
        while True:
          dato = input(msj)
          if validacion_nombre(dato):
            break
          msj = "Re-ingrese el nuevo nombre del paciente: "
        lista_pacientes[i][1] = dato.capitalize()
      elif str(pregunta) == "3":
        msj = "Ingrese la nueva edad del paciente: "
        while True:
          try:
            dato = int(input(msj))
            if validacion_menores(dato):
              break
            else:
              print('ERROR. La clínica no acepta pacientes menores de edad.')
          except:
            print('ERROR. La edad debe ser un número entero. Sin caracteres alfabeticos ni especiales.')
          msj = "Re-ingrese la nueva edad del paciente: "
        lista_pacientes[i][2] = str(dato)
      print(lista_pacientes)
  else:
    print('Dicho DNI no se encuentra registrado en nuestro sistema.')
  # PREGUNTA DE NUEVO SI SE QUIERE REPETIR LA MODIFICACIÓN     
  validacion = input("¿Quiere modificar un dato mas? (yes | no): ").lower()
  while not yes_no(validacion):
    print('ERROR. Por favor elija una opción válida.')
    validacion = input("¿Quiere seguir modificando datos? (yes | no): ").lower()
  if validacion == "yes":
    main()
