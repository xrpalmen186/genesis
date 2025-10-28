from datetime import date

current_date = date.today()
current_year = current_date.year

class Persona():
    def __init__(self, nombre, apellido, fn) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.fn = fn
    
    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre} ({self.get_edad} años)"
    
    @property
    def get_edad(self) -> int:
        return current_year - self.fn
    
    @property
    def get_nombre(self) -> str:
        return self.nombre
    
    @property
    def get_apellido(self) -> str:
        return self.apellido
    
    @property
    def get_nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"


class Asignatura():
    def __init__(self, nombre, horas, profesor) -> None:
        self.nombre = nombre
        self.horas = horas
        self.profesor = profesor
    
    def __str__(self) -> str:
        return f"La asignatura '{self.nombre}' tiene {self.horas} horas y es impartida por {self.profesor}"


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad) -> None:
        super().__init__(nombre, apellido, edad)
        self.asignaturas = []
        
    def add_asignatura(self, *nuevas_asignatura):
        for nueva_asignatura in nuevas_asignatura:
            self.asignaturas.append(nueva_asignatura)
        
    def mostrar_profesores(self):
        res = []
        for a in self.asignaturas:
            if not a.profesor.nombre in res:
                res.append(a.profesor.nombre)
        
        for p in res:
            print(p)
        
        
    def __str__(self):
        asignaturaString = ""
        
        for asignatura in self.asignaturas:
            asignaturaString += str(asignatura)
        
        return super().__str__() + " y estudia " + asignaturaString

class Grupo():
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
        
    def add_estudiante(self, alumno):
        self.estudiantes.append(alumno)
    
    def mostrar_profesores(self):
        res = []
        print(f"Profesores del grupo {self.nombre}")
        for a in self.estudiantes:
            res.append(a.mostrar_profesores())
        
        res = set(res)
            
class Profesor(Persona):
    def __init__(self, nombre, apellido, edad) -> None:
        super().__init__(nombre, apellido, edad)
        self.impartir = []
        
    def add_imparte(self, *nuevas_asignatura):
        for nueva_asignatura in nuevas_asignatura:
            self.impartir.append(nueva_asignatura.nombre)
        
    def __str__(self):
        return super().__str__() + " e imparte " + str(self.impartir)



ray = Persona("Ray", "Palma", 2006)
print(ray)



manuel = Estudiante("Manuel", "Fernandez", 2005)
print(manuel.get_edad)
print(manuel.get_nombre_completo)

alicia = Estudiante("Alicia", "Gonzalez", 2000)


josei = Profesor("Jose", "Ignacio", 1985)
david = Profesor("David", "Devega", 1980)

servidor = Asignatura("Servidor", 200, josei)
cliente = Asignatura("Cliente", 150, david)

manuel.add_asignatura(servidor, cliente)
print(manuel)

alicia.add_asignatura(servidor)
print(alicia)

josei.add_imparte(servidor)
david.add_imparte(cliente)

manuel.mostrar_profesores()
alicia.mostrar_profesores()

daw = Grupo("2DAW")



daw.add_estudiante(manuel)
daw.add_estudiante(alicia)

daw.mostrar_profesores()

print(josei)
print(david)

