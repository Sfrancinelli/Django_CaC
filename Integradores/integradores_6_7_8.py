# Ejercicio 6
class Persona():
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre

    @property
    def edad(self):
        return self.edad

    @edad.setter
    def edad(self, edad):
        self.edad = edad
    
    @property
    def dni(self):
        return self.dni   

    @dni.setter
    def dni(self, dni):
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

    @property
    def titular(self):
        return self.__titular

    @property   
    def cantidad(self):
        return self.__cantidad

    @titular.setter  
    def titular(self, titular):
        self.__titular = titular

    def mostrar(self):
        print(f"Titular: {self.__titular}.\nCantidad: ${self.__cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad

# Ejercicio 8
class CuentaJoven(Cuenta):
    def __init__(self, titular:str, edad:int, cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion 
        self.edad = edad

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter  
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    @property
    def edad(self):
        return self.edad
    
    @edad.setter
    def edad(self, edad):
        self.edad = edad

    def es_titular_valido(self):
        return self.edad >= 18 and self.edad < 25
    
    def ingresar(self, cantidad):
        super().ingresar(cantidad)

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
            print(f"Se retiraron ${cantidad}")
        else:
            print("Edad inválida. Debe ser mayor de 18 y menor de 25 años.")

    def mostrar(self):
        super().mostrar()
        print("Cuenta Joven")
        print("Bonificación:", self.__bonificacion)


def main():

    cuenta = CuentaJoven("Sebastián", 22, 50_000)
    print(cuenta.cantidad)

    cuenta.ingresar(20_000)
    print(cuenta.cantidad)

    cuenta.retirar(30_000)
    print(cuenta.cantidad)

    cuenta.set_edad(55)
    cuenta.retirar(30_000)
    print(cuenta.cantidad)

    cuenta.titular = "Sebastián Francinelli"
    print(cuenta.titular)
    cuenta.mostrar()

if __name__ == "__main__":  
    main()
