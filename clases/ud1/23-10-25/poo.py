class Pelicula():
    def __init__(self, titulo, director, anio) -> None:
        self.titulo = titulo
        self.director = director
        self.anio = anio
        
    def __str__(self) -> str:
        return f"{self.titulo} del director {self.director} ({self.anio})"
    
    def actualizar_anio(self, anio):
        self.anio = anio
        
    def actualizar_director(self, director):
        self.director = director
    
    def actualizar_titulo(self, titulo):
        self.titulo = titulo

class Biblioteca():
    def __init__(self) -> list:
        self.peliculas = []

    def add(self, pelicula):
        self.peliculas.append(pelicula)
    
    def show(self):
        for pelicula in self.peliculas:
            print(pelicula)
    
    def filtrar_por_anio(self, anio):
        return [str(p) for p in self.peliculas if p.anio == anio]   
    
    def filtrar_por_director(self, director):
        return [str(p) for p in self.peliculas if p.director == director]
    
    def buscar(self, titulo):
        return [str(p) for p in self.peliculas if p.titulo == titulo]


pelicula1 = Pelicula("Interstellar", "Christopher Nolan", 2014)
pelicula2 = Pelicula("Avatar", "James Cameron", 2009)
pelicula3 = Pelicula("Prueba", "Dani", 2349)

biblioteca = Biblioteca()

biblioteca.add(pelicula1)
biblioteca.add(pelicula2)
biblioteca.add(pelicula3)

# for pelicula in biblioteca.peliculas:
#     print(pelicula)

biblioteca.show()

print(biblioteca.filtrar_por_anio(2009))

print(biblioteca.filtrar_por_director("Dani"))

print(bi)

# listapeliculas = []

# listapeliculas.append(pelicula1)
# listapeliculas.append(pelicula2)
# listapeliculas.append(pelicula3)

# biblioteca = BibliotecaPeliculas(listapeliculas)

# # print(biblioteca.peliculas[0].titulo)

# for pelicula in biblioteca.peliculas:
#     print(f"{pelicula.titulo} del director {pelicula.director} ({pelicula.anio})")