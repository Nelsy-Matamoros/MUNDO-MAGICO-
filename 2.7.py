class FileHandler:
    def __init__(self, file_name, mode):
        """
        Constructor de la clase FileHandler.
        Inicializa los atributos del objeto y abre el archivo.

        :param file_name: Nombre del archivo a abrir.
        :param mode: Modo en el que se abrirá el archivo (e.g., 'r' para lectura, 'w' para escritura).
        """
        self.file_name = file_name
        self.mode = mode
        self.file = None
        self.open_file()
        print(f"Archivo '{self.file_name}' abierto en modo '{self.mode}'.")

    def open_file(self):
        """Método para abrir el archivo."""
        try:
            self.file = open(self.file_name, self.mode)
        except IOError as e:
            print(f"No se pudo abrir el archivo {self.file_name}: {e}")

    def write_data(self, data):
        """
        Método para escribir datos en el archivo.

        :param data: Datos a escribir en el archivo.
        """
        if self.file and self.mode == 'w':
            self.file.write(data)
            print(f"Datos escritos en el archivo '{self.file_name}'.")
        else:
            print("El archivo no está abierto en modo escritura.")

    def read_data(self):
        """
        Método para leer datos del archivo.

        :return: Datos leídos del archivo.
        """
        if self.file and self.mode == 'r':
            return self.file.read()
        else:
            print("El archivo no está abierto en modo lectura.")
            return None

    def __del__(self):
        """
        Destructor de la clase FileHandler.
        Se asegura de cerrar el archivo si está abierto.
        """
        if self.file:
            self.file.close()
            print(f"Archivo '{self.file_name}' cerrado.")
        else:
            print("El archivo ya estaba cerrado o no se había abierto.")


# Uso de la clase FileHandler
if __name__ == "__main__":
    # Crear un objeto FileHandler para escribir en un archivo
    file_writer = FileHandler('example.txt', 'w')
    file_writer.write_data('Hola, mundo!\n')

    # Crear un objeto FileHandler para leer del archivo
    file_reader = FileHandler('example.txt', 'r')
    content = file_reader.read_data()
    if content:
        print(f"Contenido del archivo: {content}")

    # Los destructores se llamarán automáticamente cuando los objetos sean destruidos
