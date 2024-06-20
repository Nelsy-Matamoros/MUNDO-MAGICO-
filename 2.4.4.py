class Carro:
    def __init__(self, modelo, anio):
        self.modelo = modelo
        self.anio = anio
        self.conductor = None  # Inicialmente, el carro no tiene conductor

    def asignar_conductor(self, persona):
        if isinstance(persona, Persona):
            self.conductor = persona

    def __str__(self):
        return f'Carro {self.modelo} del año {self.anio}, conducido por {self.conductor.nombre if self.conductor else "nadie"}.'


class Persona:
    def __init__(self, nombre, licencia):
        self.nombre = nombre
        self.licencia = licencia

    def __str__(self):
        return f'Persona {self.nombre} con licencia número {self.licencia}.'


# Creación de objetos
carro1 = Carro('Ford Ranger', 2019)
carro2 = Carro('Mitsubishi', 2020)
persona = Persona('Nelsy', 3)

# Asignar un conductor al carro
carro1.asignar_conductor(persona)
carro2.asignar_conductor(persona)
