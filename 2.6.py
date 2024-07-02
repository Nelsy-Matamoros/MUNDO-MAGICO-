class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self._marca = marca  # Atributo protegido
        self._modelo = modelo  # Atributo protegido
        self._anio = anio  # Atributo protegido

    def descripcion(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._anio}"
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, numero_puertas):
        super().__init__(marca, modelo, anio)
        self._numero_puertas = numero_puertas  # Atributo protegido

    # Sobrescritura de método (polimorfismo)
    def descripcion(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._anio}, Puertas: {self._numero_puertas}"
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo_motor):
        super().__init__(marca, modelo, anio)
        self._tipo_motor = tipo_motor  # Atributo protegido

    # Sobrescritura de método (polimorfismo)
    def descripcion(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._anio}, Tipo de motor: {self._tipo_motor}"
def imprimir_descripcion(vehiculo):
    print(vehiculo.descripcion())

# Creación de instancias y uso de métodos
auto = Auto("Toyota", "Corolla", 2020, 4)
moto = Motocicleta("Yamaha", "MT-07", 2021, "600cc")
# Uso de polimorfismo
imprimir_descripcion(auto)
imprimir_descripcion(moto)
