class debaja:
    def init(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
   
def DeBaja (pacientestxt, debajatxt, dni):
     m = open(debajatxt, "wb") #si no es binario que solo sea w
     for i in range (len(pacientestxt)): #teniendo en cuenta que pacientestxt ya esta abierto afuera, sino hay que hacerlo en la misma funcion
          if dni in pacientestxt [i][0]:
               dni = pacientestxt [i][0] 
               nombre = pacientestxt [i][1]
               edad = pacientestxt [i][2]
               val = debaja(dni, nombre, edad)
               write.dump(val, m)
