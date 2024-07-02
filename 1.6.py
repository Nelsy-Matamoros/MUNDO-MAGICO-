class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self._marca = marca  # Atributo protegido
        self._modelo = modelo  # Atributo protegido
        self._anio = anio  # Atributo protegido

    def descripcion(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._anio}"





