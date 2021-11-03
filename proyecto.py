# app principal --> integración de módulos
import pantallas.reg_paciente as registro_p
import pantallas.menu as menu
import pantallas.login as log
import pantallas.mod_paciente as mod_p
import pantallas.listar_paciente as listar_p
import pantallas.baja_paciente as baja_p
import pantallas.eliminar_turno as elim_p
import pantallas.reg_turno as reg_t
import pantallas.modificar_turno as mod_t
import pantallas.buscar_turno as busc_t
from extra.ascii_decoracion import logo, titulo_mod_p, titulo_reg_p, titulo_listar_p, titulo_baja_p, titulo_mod_t, titulo_reg_t, titulo_eliminar_t, titulo_buscar_t
from time import sleep
from os import system
clear = lambda: system('cls')

print(logo)
sleep(3)
clear()
ingreso = log.login() # login
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
            # baja de pacientes
            print(titulo_baja_p)
            baja_p.baja_paciente()
        elif opcion == 3:
            # eliminar turnos
            print(titulo_eliminar_t)
            elim_p.mod_eliminar_t()
        elif opcion == 1:
            # registrar turnos
            print(titulo_reg_t)
            reg_t.reg_turno()
        elif opcion == 2:
            # modificar turnos
            print(titulo_mod_t)
            mod_t.modificar_turno()
        elif opcion == 9:
            # buscar turnos
            print(titulo_buscar_t)
            busc_t.__main__()
        clear()
        opcion = menu.consulta_opcion()