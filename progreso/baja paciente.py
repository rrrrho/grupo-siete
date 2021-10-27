import os; clear = lambda: os.system('cls'); clear(); import random;

#Funcion Baja del Paciente
def baja_paciente(lista_pacientes):
    dni = int(input("Ingrese el numero de DNI del paciente: "))
    encontrar = False
    for i in range(len(lista_pacientes)):
        if str(dni) in lista_pacientes[i][0]:
            lista_bajas.append(lista_pacientes[i])
            lista_pacientes.pop(i)
            encontrar = True
            pregunta = input("Desea dar de baja a un paciente mas? (yes | no): ")
            if pregunta == "yes":
                baja_paciente(lista_pacientes)
            else:
                break
    if encontrar == True:
        print(f"El/Los Pacientes que se dieron de baja son: {lista_bajas}")
        return lista_pacientes
    elif encontrar == False:
        print("El DNI ingresado no se encuentra registrado en nuestra base de datos")
        return lista_pacientes

#PP
pacientes = [ ["46623410", "Martin", "45"] , ["25820887", "José", "64"] , ["12345678", "Raul", "22"] ]
print(pacientes)
lista_bajas = []
baja_paciente(pacientes)
print(pacientes)