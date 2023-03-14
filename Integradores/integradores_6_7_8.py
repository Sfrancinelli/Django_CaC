class Persona():
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad
    
    def get_dni(self):
        return self.dni   

    def set_dni(self, dni):
        self.dni = dni

    def mostrar(self):
        return f"Nombre: {self.nombre}.\nEdad: {self.edad}.\nDNI: {self.dni}"    
    
    def es_mayor(self):
        if self.edad >= 18:
            return True
        else:
            return False


def main():
     
    persona = Persona()

    print(persona.get_nombre())
    print(persona.get_edad())
    print(persona.get_dni())

    persona.set_nombre("Sebastián")
    persona.set_edad(22)
    persona.set_dni("43081141")

    print(persona.get_nombre())
    print(persona.get_edad())
    print(persona.get_dni())

    print(persona.mostrar())
    print(persona.es_mayor())

if __name__ == "__main__":  
    main()
