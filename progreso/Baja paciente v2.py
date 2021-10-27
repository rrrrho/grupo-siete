import os; clear = lambda: os.system('cls'); clear(); import random;
#La función de Ulises que la modifique para que funcione, hasta ahora intenté asegurarme de que no ocurra ningun error
#Funcion
def baja_paciente(lista_pacientes, lista_bajas):
    flag = True
    while flag == True:
        try:
            dni = input("Ingresar numero de DNI (introducir no para finalizar la baja de pacientes):")
            #dni= str(dni)
            i = 0
            while dni != 'no':
                if dni == lista_pacientes[i][0]:
                    lista_bajas.append(lista_pacientes[i]) #Si lista bajas no se usa, eliminar esta linea y tambien lista_bajas de parametros de la funcion
                    lista_pacientes.pop(i)
                    print("DNI eliminado...")
                    i= 0
                else:
                    i= i + 1
                    continue
                dni = input("Ingresar numero de DNI (introducir no para finalizar la baja de pacientes):")
            flag = False
        except IndexError:
            print("No se ha encontrado el DNI")
            continue

pacientes = [ ["46623410", "Martin", "45"] , ["25820887", "José", "64"] , ["12345678", "Raul", "22"] ]
print(pacientes)
bajas= []
baja_paciente(pacientes, bajas)
print(pacientes)
print(bajas)