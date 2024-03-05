## Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperatura  = [
    [    # ciudad 1 quito
        [    #Semana1
            { "día" : "Lunes" , "temperatura" : 10 },
            { "día" : "Martes" , "temperatura" : 18 },
            { "día" : "Miércoles" , "temp" : 12 },
            { "día" : "Jueves" , "temp" : 8 },
            { "día" : "Viernes" , "temperatura" : 10 },
            { "día" : "Sábado" , "temp" : 12 },
            { "día" : "Domingo" , "temperatura" : 15 }
        ],
        [    #Semana2
            { "día" : "lunes" , "temperatura" : 8 },
            { "día" : "Martes" , "temperatura" : 10 },
            { "día" : "Miércoles" , "temp" : 12 },
            { "día" : "Jueves" , "temp" : 15 },
            { "día" : "Viernes" , "temperatura" : 18 },
            { "día" : "Sábado" , "temp" : 15 },
            { "día" : "Domingo" , "temperatura" : 15 }
        ],
        [    #Semana3
            { "día" : "lunes" , "temperatura" : 9 },
            { "día" : "Martes" , "temperatura" : 12 },
            { "día" : "Miércoles" , "temp" : 20 },
            { "día" : "Jueves" , "temp" : 15 },
            { "día" : "Viernes" , "temperatura" : 10 },
            { "día" : "Sábado" , "temp" : 15 },
            { "día" : "Domingo" , "temperatura" : 10 }
        ],
        [    #Semana4
            { "día" : "lunes" , "temperatura" : 8 },
            { "día" : "Martes" , "temperatura" : 12 },
            { "día" : "Miércoles" , "temp" : 15 },
            { "día" : "Jueves" , "temp" : 15 },
            { "día" : "Viernes" , "temperatura" : 12 },
            { "día" : "Sábado" , "temp" : 10 },
            { "día" : "Domingo" , "temperatura" : 10 }
        ]
    ],
    [    #Ciudad 2Puyo
        [    #Semana1
            { "día" : "Lunes" , "temperatura" : 18 },
            { "día" : "Martes" , "temperatura" : 18 },
            { "día" : "Miércoles" , "temp" : 19 },
            { "día" : "Jueves" , "temp" : 18 },
            { "día" : "Viernes" , "temperatura" : 17 },
            { "día" : "Sábado" , "temp" : 18 },
            { "día" : "Domingo" , "temperatura" : 18 }
        ],
        [    #Semana2
            { "día" : "Lunes" , "temperatura" : 18 },
            { "día" : "Martes" , "temperatura" : 18 },
            { "día" : "Miércoles" , "temp" : 19 },
            { "día" : "Jueves" , "temp" : 17 },
            { "día" : "Viernes" , "temperatura" : 18 },
            { "día" : "Sábado" , "temp" : 18 },
            { "día" : "Domingo" , "temperatura" : 18 }
        ],
        [    #Semana3
            { "día" : "Lunes" , "temperatura" : 28 },
            { "día" : "Martes" , "temperatura" : 26 },
            { "día" : "Miércoles" , "temp" : 28 },
            { "día" : "Jueves" , "temp" : 28 },
            { "día" : "Viernes" , "temperatura" : 26 },
            { "día" : "Sábado" , "temp" : 28 },
            { "día" : "Domingo" , "temperatura" : 28 }
        ],
        [    #Semana4
            { "día" : "Lunes" , "temperatura" : 24 },
            { "día" : "Martes" , "temperatura" : 27 },
            { "día" : "Miércoles" , "temp" : 29 },
            { "día" : "Jueves" , "temp" : 28 },
            { "día" : "Viernes" , "temperatura" : 26 },
            { "día" : "Sábado" , "temp" : 28 },
            { "día" : "Domingo" , "temperatura" : 28 }
        ]
    ],
    [    #Ciudad 3 Esmeraldas
        [    #Semana1
            { "día" : "Lunes" , "temperatura" : 20 },
            { "día" : "Martes" , "temperatura" : 29 },
            { "día" : "Miércoles" , "temp" : 29 },
            { "día" : "Jueves" , "temp" : 28 },
            { "día" : "Viernes" , "temperatura" : 28 },
            { "día" : "Sábado" , "temp" : 25 },
            { "día" : "Domingo" , "temperatura" : 22 }
        ],
        [    #Semana2
            { "día" : "Lunes" , "temperatura" : 29 },
            { "día" : "Martes" , "temperatura" : 28 },
            { "día" : "Miércoles" , "temp" : 30 },
            { "día" : "Jueves" , "temp" : 20 },
            { "día" : "Viernes" , "temperatura" : 28 },
            { "día" : "Sábado" , "temp" : 28 },
            { "día" : "Domingo" , "temperatura" : 28 }
        ],
        [    #Semana3
            { "día" : "Lunes" , "temperatura" : 28 },
            { "día" : "Martes" , "temperatura" : 28 },
            { "día" : "Miércoles" , "temp" : 28 },
            { "día" : "Jueves" , "temp" : 28 },
            { "día" : "Viernes" , "temperatura" : 29 },
            { "día" : "Sábado" , "temp" : 30 },
            { "día" : "Domingo" , "temperatura" : 28 }
        ],
        [    #Semana4
            { "día" : "Lunes" , "temperatura" : 28 },
            { "día" : "Martes" , "temperatura" : 28 },
            { "día" : "Miércoles" , "temp" : 30 },
            { "día" : "Jueves" , "temp" : 29 },
            { "día" : "Viernes" , "temperatura" : 26 },
            { "día" : "Sábado" , "temp" : 28 },
            { "día" : "Domingo" , "temperatura" : 20 }
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
            if elemento > maximo:
                maximo = elemento

# Mostrar el resultado del elemento máximo
print("El elemento máximo en las temperaturas es:", maximo)


# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Ciudad 1 Quito", "Ciudad 2 Puyo", "Ciudad 3 Esmeraldas"]
for ciudad_idx, ciudad in enumerate(temperaturas)
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")
