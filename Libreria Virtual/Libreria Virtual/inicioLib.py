class Libreria:
    def __init__(self,nombre_libros,num_estanteria,paginas_libro,autor_libro):
        self.nombre_libros = nombre_libros
        self.num_estanteria = num_estanteria
        self.paginas_libro = paginas_libro
        self.autor_libro = autor_libro
    def libros(self):
        print(input(f"El libro llamado {self.nombre_libros} ha sido guardado exitosamente"))


