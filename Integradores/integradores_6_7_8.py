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


class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular
    
    def get_cantidad(self):
        return self.__cantidad
    
    def set_titular(self, titular):
        self.__titular = titular

    def mostrar(self):
        return f"Titular: {self.__titular}.\nCantidad: {self.__cantidad}"
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad
        

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

    print("-----------------------------------------------------")

    cuenta = Cuenta("Sebastián")
    print(cuenta.get_titular())
    print(cuenta.get_cantidad())
    cuenta.set_titular("Sebastian Francinelli")

    print(cuenta.mostrar())

    cuenta.ingresar(10_000)
    print(cuenta.mostrar())
    cuenta.retirar(3_000)
    print(cuenta.mostrar())

    print("-----------------------------------------------------")


if __name__ == "__main__":  
    main()
