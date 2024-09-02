class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', id_usuario='{self.id_usuario}', libros_prestados={self.libros_prestados})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # ISBN como clave, Libro como valor
        self.usuarios = set()  # Conjunto de IDs de usuario

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
        else:
            print("El libro ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in [u.id_usuario for u in self.usuarios]:
            self.usuarios.add(usuario)
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        self.usuarios = {u for u in self.usuarios if u.id_usuario != id_usuario}

    def prestar_libro(self, id_usuario, isbn):
        usuario = self._encontrar_usuario(id_usuario)
        libro = self.libros.get(isbn)
        if usuario and libro:
            usuario.prestar_libro(libro)
            self.quitar_libro(isbn)
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        usuario = self._encontrar_usuario(id_usuario)
        libro = self._encontrar_libro(isbn)
        if usuario and libro:
            usuario.devolver_libro(libro)
            self.añadir_libro(libro)
        else:
            print("Usuario o libro no encontrado.")

    def buscar_libro(self, criterio, valor):
        resultado = [libro for libro in self.libros.values() if getattr(libro, criterio) == valor]
        return resultado

    def listar_libros_prestados(self, id_usuario):
        usuario = self._encontrar_usuario(id_usuario)
        if usuario:
            return usuario.libros_prestados
        else:
            print("Usuario no encontrado.")

    def _encontrar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def _encontrar_libro(self, isbn):
        return self.libros.get(isbn)
# Crear la biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("1984", "George Orwell", "Dystopian", "9780451524935")
libro2 = Libro("To Kill a Mockingbird", "Harper Lee", "Fiction", "9780060935467")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Crear usuario
usuario1 = Usuario("Juan Pérez", "U001")

# Registrar usuario
biblioteca.registrar_usuario(usuario1)

# Prestar libro
biblioteca.prestar_libro("U001", "9780451524935")

# Buscar libro
print(biblioteca.buscar_libro("titulo", "1984"))

# Listar libros prestados
print(biblioteca.listar_libros_prestados("U001"))

# Devolver libro
biblioteca.devolver_libro("U001", "9780451524935")
