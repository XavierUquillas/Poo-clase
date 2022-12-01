class miClase:
    x=5

p1= miClase()
print(p1.x)

class persona:
    nombre = str
    edad = int
    
    def _init_(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def _init_(self):
        return f"Su nombre es {self.nombre}"
    
    
p2 = persona("Xavier", 29)
print(p2)

    
class Persona2:
    nombre = str
    edad = int
    cedula = int
    
    def _int_(self,nombre,edad,cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        
    def mifuncion(self):
        print("Hola mi nombre es " + self.nombre + "mi numero de cedula es " + self.cedula)
        
p3= Persona2("Alexander", 30,"1728872530")
p3.mifuncion()

p3.nombre = "Carlos" 
p3.mifuncion()