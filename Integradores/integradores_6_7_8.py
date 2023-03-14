# Ejercicio 6

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

# Ejercicio 7
class Cuenta:
    def __init__(self, titular:str, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular
    
    def get_cantidad(self):
        return self.__cantidad
    
    def set_titular(self, titular):
        self.__titular = titular

    def mostrar(self):
        return f"Titular: {self.__titular}.\nCantidad: ${self.__cantidad}"
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad

# Ejercicio 8

class CuentaJoven(Cuenta):
    def __init__(self, titular:str, bonificacion:int, edad:int, cantidad=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion 
        self.edad = edad
        self.__titular = titular
        self.__cantidad = cantidad

    def get_bonificacion(self):
        return self.bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular
        return self.__titular

    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        self.edad = edad

    def get_cantidad(self):
        return self.__cantidad

    def es_titular_valido(self):
        return self.edad >= 18 and self.edad < 25
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if self.es_titular_valido():
            self.__cantidad -= cantidad
            print(f"Se retiraron ${cantidad}")
        else:
            print("Edad no válida. Debe ser mayor de 18 y menor de 25 años.")

    def mostrar(self):
        return f"Cuenta Joven.\nTitular: {self.__titular}.\nCantidad: ${self.__cantidad}.\nEdad: {self.edad}.\nBonificación: {self.bonificacion}"


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

    print(cuenta.get_cantidad())

    print("-----------------------------------------------------")

    cuenta_j = CuentaJoven("Sebastián", 10, 19)
    print(cuenta_j.get_titular())
    print(cuenta_j.get_cantidad())
    print(cuenta_j.get_bonificacion())
    print(cuenta_j.get_edad())
    cuenta_j.set_titular("Sebastian Francinelli")
    cuenta_j.set_bonificacion(50)
    cuenta_j.set_edad(50)
    cuenta_j.ingresar(500_000)

    print(cuenta_j.mostrar())
    cuenta_j.retirar(20_000)

    cuenta_j.set_edad(22)

    cuenta_j.retirar(30_000)

    print(cuenta_j.mostrar())

    print(cuenta_j.get_cantidad())



if __name__ == "__main__":  
    main()
