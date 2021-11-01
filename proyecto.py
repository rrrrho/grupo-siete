# app principal
from pantallas.baja_paciente import baja_paciente
import pantallas.reg_paciente as registro_p
import pantallas.menu as menu
import pantallas.login as log
import pantallas.mod_paciente as mod_p
import pantallas.listar_paciente as listar_p
import pantallas.baja_paciente as baja_p
from extra.ascii_decoracion import logo, titulo_mod_p, titulo_reg_p, titulo_listar_p
from time import sleep
import os
clear = lambda: os.system('cls')

print(logo)
sleep(3)
clear()
# login
ingreso = log.main()
sleep(2)

# menu de opciones
if ingreso:
    clear()
    opcion = menu.consulta_opcion()
    while opcion != 0:
        clear()
        if opcion == 4:
            # registro de pacientes
            print(titulo_reg_p)
            registro_p.reg_paciente()
        elif opcion == 5:
            # modificación de pacientes
            print(titulo_mod_p)
            mod_p.mod_pacientes()
        elif opcion == 7:
            # listar pacientes
            print(titulo_listar_p)
            listar_p.listar_p()
        elif opcion == 6:
            baja_p.baja_paciente()
        else:
            # le sigue el resto de opciones
            pass
        clear()
        opcion = menu.consulta_opcion()