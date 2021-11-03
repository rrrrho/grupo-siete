from os import remove, rename
from funciones.validaciones import validacion_dni, validacion_menores, validacion_nombre, yes_no
from funciones.arch_manipulacion import dicc_reg, mod_arch, traer_reg, paciente_diccionario, arch_dnis

def mod_pacientes():
  # modifica el archivo pacientes.txt
  dnis = arch_dnis('datos/pacientes.txt')
  msj = "Ingrese el número de DNI de la persona: "
  while True:
    try:
      dni = int(input(msj))
      if validacion_dni(dni):
        break
    except:
      print('ERROR. El DNI debe ser un número entero. Sin caracteres alfabeticos ni especiales.')
    msj = "Re-ingrese el número de DNI de la persona: "  
  if str(dni) not in dnis:
    print(f'No existe el DNI {dni} en nuestro sistema.')
  else:
    paciente = paciente_diccionario(traer_reg('datos/pacientes.txt', str(dni))) # trae el registro en formato string y luego lo convierte a diccionario
    print()
    while True:
      try:
        pregunta = int(input("¿Qué desea modificar? 1- Dni | 2- Nombre | 3- Edad: "))
        assert pregunta == 1 or pregunta == 2 or pregunta == 3
        break
      except:
        print('Por favor elija una opción válida.')
    if pregunta == 1:
      msj = "Ingrese el nuevo número de DNI del paciente: "
      while True:
        try: 
          dato = int(input(msj))
          assert str(dato) not in dnis, 'Ya existe una persona con ese DNI.'
          if validacion_dni(dato):
            break
        except AssertionError as err:
          print(err)
        except:
          print('ERROR. El DNI debe ser un número entero. Sin caracteres alfabeticos ni especiales.')
        msj = "Re-ingrese el nuevo número de DNI del paciente: "
      paciente['dni'] = str(dato)
    elif pregunta == 2:
      msj = "Ingrese el nuevo nombre (completo) del paciente: "
      while True:
        dato = input(msj).strip()
        if validacion_nombre(dato):
          break
        msj = "Re-ingrese el nuevo nombre del paciente: "
      paciente['nombre'] = dato.title()        
    elif pregunta == 3:
      msj = "Ingrese la nueva edad del paciente: "
      while True:
        try:
          dato = int(input(msj))
          assert dato > 0 and dato < 105
          if validacion_menores(dato):
            break
          else:
            print('ERROR. La clínica no acepta pacientes menores de edad.')
        except:
          print('Por favor escriba una edad válida.')
        msj = "Re-ingrese la nueva edad del paciente: "
      paciente['edad'] = str(dato)
    paciente = dicc_reg(paciente) # convierto el diccionario a formato string
    mod_arch('datos/pacientes.txt', str(dni), paciente)
    remove('datos/pacientes.txt')
    rename('datos/mod.txt', 'datos/pacientes.txt')
    print()
    print('El paciente ha sido modificado con éxito.')
  print()
  validacion = input("¿Quiere seguir modificando pacientes? (yes | no): ").lower()
  while not yes_no(validacion):
    print('ERROR. Por favor elija una opción válida.')
    validacion = input("¿Quiere seguir modificando pacientes? (yes | no): ").lower()   
  if validacion == "yes":
    print()
    mod_pacientes()