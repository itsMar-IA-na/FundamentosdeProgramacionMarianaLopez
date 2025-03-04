ciudades = ["Montañita", "Puellaro", "Cayambe", "Guayaquil"]

temperaturas = [
    [   # Montañita
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [   # Puellaro
        [   #Semana 1
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 25}
        ],
        [   #Semana 2
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 22}
        ]
    ],
    [   # Cayambe
        [   #Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 20}
        ],
        [   #Semana 2
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 19}
        ]
    ],
    [   # Guayquil
        [   # Semana 1
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 32}
        ],
        [   #Semana 2
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 32}
        ]
    ]
]

for ciudad_idx, ciudad in enumerate(temperaturas):
    print(f"\nNombre de la ciudad: {ciudades[ciudad_idx]}")
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"  En la semana {semana_idx + 1} el promedio de tempetarutas es: {promedio:.2f}°C")
