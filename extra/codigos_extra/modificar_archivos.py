from funciones.arch_manipulacion import traer_reg, mod_arch, reg_diccionario, dicc_reg
from os import remove, rename

registro = traer_reg('datos/pacientes.txt', '32446267') # trae el registro del paciente con x DNI (string)
'''
'32446267;pepito;56'
'''
registro = reg_diccionario(registro) # lo convierte a diccionario. string -> diccionario
'''
obj = {
  'dni': '32446267',
  'nombre': 'pepito',
  'edad': '56'
}
'''
registro['edad'] = '987' # modifica el valor de la clave edad
registro = dicc_reg(registro) # convierte el diccionario nuevamente a string
'''
'32446267;pepito;987'
'''
mod_arch('datos/pacientes.txt', '30126875', registro) # crea un archivo mod.txt con las modificaciones hechas en la carpeta datos
# NOTA: si en el tercer argumento especificamos un string vacio elimina el registro
remove('datos/pacientes.txt') # IMPORTANTE eliinamos el archivo pacientes.txt antiguo
rename('datos/mod.txt', 'datos/pacientes.txt') # renombramos mod.txt como pacientes.txt. hay que especificar la carpeta donde va a quedar

