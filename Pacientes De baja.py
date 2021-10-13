listaPacientes=[]
listaDeBaja=[]
i=1
while (i==1):
    Pacientes=int(input("Ingrese el número del paciente para saber si esta de alta (0) o que tiene que ser atendido (1), en caso de que no alla mas pacientes ingrese -1"))
    if (Pacientes==-1):
        print(listaPacientes)
        i=0
    if (Pacientes<0 or Pacientes>1):
        print="Ingrese un número valido"
    else:
        listaPacientes.append(Pacientes)

for x in listaPacientes:
    if (x==0):
        PacienteDeAlta=x
        listaDeBaja.append(PacienteDeAlta)
        