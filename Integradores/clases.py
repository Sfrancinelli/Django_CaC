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

print(10*'-----')

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

    @property
    def salario(self):
        return self.__salario
    
    # La función repr muestra el objeto de acuerdo al return asignado
    # en vez de mostrarlo como siempre (<object at 0x...>)
    def __repr__(self) -> str:
        return self.nombre_completo
    
class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, apellido, horas_trabajadas, valor_hora):
        super().__init__(nombre, apellido)
        self.__horas_trabajadas = horas_trabajadas
        self.__valor_hora = valor_hora

    @property
    def salario(self):
        return self.__horas_trabajadas * self.__valor_hora
    
    # La función repr muestra el objeto de acuerdo al return asignado
    # en vez de mostrarlo como siempre (<object at 0x...>)
    def __repr__(self) -> str:
        return self.nombre_completo
    
class EmpleadoPasante(Empleado):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)

    @property
    def salario(self):
        return 0

    def __repr__(self) -> str:
        return self.nombre_completo

class Nomina:
    def __init__(self):
        self._lista_empleados = []

    def agregar_empleado(self, empleado):
        self._lista_empleados.append(empleado)

    def print(self):
        for empleado in self._lista_empleados:
            if isinstance(empleado, Empleado):
                print(f"{empleado.nombre_completo} \t ${empleado.salario}")
            else:
                print(f"En la nómina hay un no empleado: {empleado}")

nomina_empleados = Nomina()

nomina_empleados.agregar_empleado(EmpleadoFullTime('Lucas', 'Pratto', 6000))
nomina_empleados.agregar_empleado(EmpleadoFullTime('Luca', 'Janson', 6500))
nomina_empleados.agregar_empleado(EmpleadoPorHora('Valentin', 'Gomez', 200, 50))
nomina_empleados.agregar_empleado(EmpleadoPorHora('Walter', 'Bou', 150, 100))
nomina_empleados.agregar_empleado(EmpleadoPorHora('Santiago', 'Caseres', 100, 150))
# UN empleado no se puede instanciar porque es una clase abstracta
# nomina_empleados.agregar_empleado(Empleado('Diego', 'Armando', 10))
# Si tiene la implementación de salario si se puede instanciar, sino no.
# nomina_empleados.agregar_empleado(EmpleadoPasante('Diego', 'Godin'))

nomina_empleados.print()

# Herencia múltiple

class Estudiante():
    """Clase estudiantes"""
    def __init__(self, legajo):
        self.__legajo = legajo

    @property
    def legajo(self):
        return self.__legajo

    def __str__(self):
        return f"Legajo: {self.__legajo}"
class EstudiantePasante(Empleado, Estudiante):
    def __init__(self, nombre, apellido, legajo):
        Empleado.__init__(self, nombre, apellido)
        Estudiante.__init__(self, legajo)

    # Tengo que implementar la propiedad salario porque hereda de empleado
    @property
    def salario(self):
        return 0
    
    def __str__(self) -> str:
        return f"{self.nombre_completo}. Legajo: {self.legajo}"
    
mis_estudiantes = []
mis_estudiantes.append()