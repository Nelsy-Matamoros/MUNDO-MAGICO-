class RegistroClima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura_diaria(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas) != 7:
            print("Error: Deben ingresar 7 temperaturas diarias para calcular el promedio semanal.")
            return None
        else:
            return sum(self.temperaturas) / 7

def main():
    registro = RegistroClima()
    for dia in range(7):
        temperatura = float(input(f"Ingrese la temperatura para el día {dia + 1}: "))
        registro.ingresar_temperatura_diaria(temperatura)
    promedio_semanal = registro.calcular_promedio_semanal()
    if promedio_semanal is not None:
        print("El promedio semanal de temperaturas es:", promedio_semanal)

if __name__ == "__main__":
    main()
