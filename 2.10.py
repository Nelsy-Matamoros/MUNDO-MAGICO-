class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    codigo, nombre, cantidad = linea.strip().split(',')
                    self.productos[codigo] = {'nombre': nombre, 'cantidad': int(cantidad)}
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no existe. Se creará uno nuevo.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for codigo, datos in self.productos.items():
                    file.write(f"{codigo},{datos['nombre']},{datos['cantidad']}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("No tienes permiso para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, codigo, nombre, cantidad):
        self.productos[codigo] = {'nombre': nombre, 'cantidad': cantidad}
        self.guardar_inventario()

    def actualizar_producto(self, codigo, nombre=None, cantidad=None):
        if codigo in self.productos:
            if nombre:
                self.productos[codigo]['nombre'] = nombre
            if cantidad is not None:
                self.productos[codigo]['cantidad'] = cantidad
            self.guardar_inventario()
        else:
            print(f"Producto con código {codigo} no encontrado.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_inventario()
            print(f"Producto con código {codigo} eliminado.")
        else:
            print(f"Producto con código {codigo} no encontrado.")


# Ejemplo de uso
def main():
    inventario = Inventario()

    # Agregar productos
    inventario.agregar_producto('001', 'Chocolate', 50)
    inventario.agregar_producto('002', 'Vainilla', 30)

    # Actualizar un producto
    inventario.actualizar_producto('001', cantidad=45)

    # Eliminar un producto
    inventario.eliminar_producto('002')

    # Mostrar el inventario actual
    print(inventario.productos)


if __name__ == "__main__":
    main()
