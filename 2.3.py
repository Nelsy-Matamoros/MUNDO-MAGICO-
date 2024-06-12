
def ingresar_temperaturas_diarias():
    temperaturas = []
    for dia in range(7):
        temperatura = float(input(f"Ingrese la temperatura para el día {dia + 1}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

def main():
    temperaturas = ingresar_temperaturas_diarias()
    promedio_semanal = calcular_promedio_semanal(temperaturas)
    print("El promedio semanal de temperaturas es:", promedio_semanal)

if __name__ == "__main__":
    main()
