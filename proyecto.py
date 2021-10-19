# app principal
import pantallas.reg_paciente as registro_p
import pantallas.menu as menu
import pantallas.login as log
import pantallas.mod_paciente as mod_p
from time import sleep
import os
clear = lambda: os.system('cls')

# LOGIN
clear()
ingreso = log.main()
sleep(2)

# MENU DE OPCIONES
if ingreso:
    clear()
    opcion = menu.consulta_opcion()
    while opcion != 0:
        clear()
        # REGISTRO DE PACIENTES
        if opcion == 4:
            registro_p.main()
        # MODIFICACIÓN DE PACIENTES
        elif opcion == 5:
            mod_p.main()
        else:
            pass
            # le sigue el resto de opciones
        clear()
        opcion = menu.consulta_opcion()