from funciones.validacionesTurnos import valPaciente, valDNI, valMes, valDia, valHora, valTurno
from funciones.arch_manipulacion import escribir_fichero

def reg_turno():
    print("Registro de turnos inicializado. A considerar: \nDias no disponibles: 1, 8, 15, 22 \nHorario permitido: De 10:00 a 14:00 \nDuracion del turno: 15 minutos")
    print("*"*40, "\n")
    while True:
        try:
            dniTurno = input("Ingresar DNI del paciente: ")
            while valDNI(dniTurno)==False:
                dniTurno = input("Ingresar un DNI válido [8 dígitos]: ")
            assert (valPaciente(dniTurno,'datos/pacientes.txt')==True), "Se ingresó un DNI que no pertenece a ningún paciente en la base de datos. Verificar que el paciente este registrado"
            assert (valPaciente(dniTurno,'datos/turnos.txt')==False), "Se ingresó un DNI que ya tiene un turno asignado"
                
            mesTurno = input("Ingresar Mes de turno: ")
            while valMes(mesTurno) == False:
                mesTurno = input("Ingresar un Mes válido para el turno: ")
                
            diaTurno = input("Ingresar Día del turno: ").title()
            while valDia(diaTurno, mesTurno.title())==False:
                diaTurno= input("Ingresar un número de día válido para el mes ingresado: ")
            assert int(diaTurno) not in [1,8,15,22], "Se ingresó un día en el que el médico no trabaja"
            
            horaTurno= input("Ingresar Hora del turno (horas:minutos): ")
            while valHora(horaTurno)==False:
                horaTurno= input("Ingresar una hora válida para el turno: ")
            horaComparar = int(horaTurno.replace(":",""))
            assert (1000<=horaComparar<=1400), "Se ingresó un horario en el que el médico no trabaja"
            
            if valTurno(mesTurno.title(),diaTurno,horaTurno)==True:
                try:
                    print(f'Registrando el siguiente turno: {diaTurno} de {mesTurno.title()} a las {horaTurno} para el paciente de DNI {dniTurno}')
                    escribir_fichero('datos/turnos.txt', f'{dniTurno};{mesTurno.title()};{diaTurno};{horaTurno}', 'a')
                except FileNotFoundError:
                    print('No se encontró el archivo de turnos en el directorio específicado')
                else:
                    print()
                    print('El turno ha sido registrado con éxito:')
            else:
                print("Error al registrar el turno: La fecha y horario del turno ingresado entran en conflicto con otro turno")
        except AssertionError as error:
            print("Error al registrar el turno:",error)
        finally:
            print()
            decision = input("Registrar otro turno? (s/n): ")
            while decision not in ("s","n"):
                decision = input("Ingresar una opción válida. Opciones -> s - Si; n - No :")
            if decision == "n":
                print("Finalizando el registro..")
                break
            print()
