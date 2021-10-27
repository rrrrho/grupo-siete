import os; clear = lambda: os.system('cls'); clear()
from funciones.validaciones import validacion_dni, validacion_menores, validacion_nombre, yes_no
from funciones.arch_manipulacion import dicc_reg, mod_arch, traer_reg, reg_diccionario, arch_dnis


def mod_pacientes():
  # modifica el archivo pacientes.txt de la carpeta datos
  dnis = arch_dnis('datos/pacientes.txt')
  msj = "Ingrese el número de DNI de la persona: "
  while True:
    try:
      dni = int(input(msj))
      if validacion_dni(dni):
        break
    except ValueError:
      print('ERROR. El DNI debe ser un número entero. Sin caracteres alfabeticos ni especiales.')
    msj = "Re-ingrese el número de DNI de la persona: "
  i = 0
  encontrado = False
  while encontrado != True and i < len(dnis):
    if dnis[i][0] == str(dni): # verificar tipo de dato de dni
      encontrado = True
    i += 1    
  if not encontrado:
    print(f'No existe el DNI {dni} en nuestro sistema.')
  else:
    paciente = reg_diccionario(traer_reg('datos/pacientes.txt', str(dni)))
    while True:
      try:
        pregunta = int(input("¿Qué desea modificar? 1- Dni | 2- Nombre | 3- Edad: "))
        assert pregunta == 1 or pregunta == 2 or pregunta == 3
        break
      except:
        print('ERROR. Por favor elija una opción válida.')
    if pregunta == 1:
      msj = "Ingrese el nuevo número de DNI del paciente: "
      while True:
        try:
          encontrado = False
          i = 0    
          dato = int(input(msj))
          while encontrado != True and i < len(dnis):
            if str(dato) == dnis[i][0]:
              encontrado = True
            i += 1
          assert not encontrado, 'Ya existe una persona con ese DNI.'
          if validacion_dni(dato):
            break
        except AssertionError as err:
          print(err)
        except:
          print('ERROR. El DNI debe ser un número entero. Sin caracteres alfabeticos ni especiales.')
        msj = "Re-ingrese el nuevo número de DNI del paciente: "
      paciente['dni'] = str(dato)
    elif pregunta == 2:
      msj = "Ingrese el nuevo nombre del paciente: "
      while True:
        dato = input(msj)
        if validacion_nombre(dato):
          break
        msj = "Re-ingrese el nuevo nombre del paciente: "
      paciente['nombre'] = dato.capitalize()        
    elif pregunta == 3:
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
      paciente['edad'] = str(dato)
    paciente = dicc_reg(paciente)
    mod_arch('datos/pacientes.txt', str(dni), paciente)
    os.remove('datos/pacientes.txt')
    os.rename('datos/mod.txt', 'datos/pacientes.txt')
  validacion = input("¿Quiere modificar un dato mas? (yes | no): ").lower()
  while not yes_no(validacion):
    print('ERROR. Por favor elija una opción válida.')
    validacion = input("¿Quiere seguir modificando datos? (yes | no): ").lower()   
  if validacion == "yes":
    mod_pacientes()