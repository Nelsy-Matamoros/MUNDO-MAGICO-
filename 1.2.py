# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # ciudad 1 Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 8},
            {"day": "Viernes", "temp": 10},
            {"day": "Sábado", "temp": 12},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 8},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 10},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 10}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 8},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 10},
            {"day": "Domingo", "temp": 10}
        ]
    ],
    [   # Ciudad 2 Puyo
        [   # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 28}
        ]
    ],
    [   # Ciudad 3 Esmeraldas
        [   # Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 20}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana


for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)


# Inicializar la variable "maximo" con el valor mínimo posible
maximo = float('-inf')

# Iterar a través de capas, filas y columnas para encontrar el elemento máximo
for capa in temperaturas:
    for fila in capa:
        for elemento in fila:

                maximo = elemento

# Mostrar el resultado del elemento máximo
print("El elemento máximo en las temperaturas es:", maximo)

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Ciudad 1 Quito", "Ciudad 2 Puyo", "Ciudad 3 Esmeraldas"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")











