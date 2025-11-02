class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando.")
        

estudiante1 = Estudiante("Juan", 15, 3)
estudiante1.estudiar()