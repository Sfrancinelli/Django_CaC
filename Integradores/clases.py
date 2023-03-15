from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, apellido, dni, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    @abstractmethod
    def registrarse(self):
        pass

    @abstractmethod
    def save(self):
        pass

class Estudiante(Persona):
    def __init__(self, nombre, apellido, dni, email, matricula, baja):
        super().__init__(nombre, apellido, dni, email)
        self.matricula = matricula
        self.baja = baja

    def registrarse(self):
        print("Registro de estudiante")

    def save(self):
        pass

    def soft_delete(self):
        pass

class Docente(Persona):
    def __init__(self, nombre, apellido, dni, email, legajo):
        super().__init__(nombre, apellido, dni, email)
        self.legajo = legajo

    def registrarse(self):
        print("Registro de docente")

    def save(self):
        pass

nuevo_estudiante = Estudiante("Raul", "Lopez", "43083382", "raullopez@gmail.com", "113344", False)
print(nuevo_estudiante)
nuevo_estudiante.registrarse()

nuevo_docente = Docente("Carlos", "Gómez", "32456789", "Carlosgomez@gmail.com", 1122345)
nuevo_docente.registrarse()
print(nuevo_docente)

class Empleado(ABC):
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    @property
    @abstractmethod
    def salario(self):
        pass


class EmpleadoFullTime(Empleado):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido)
        self.__salario = salario