# ejercicios.py

ejercicios_disponibles = [
    {
        "id": "suma_simple",
        "descripcion": "Calcula la suma de 5 y 3.",
        "codigo_inicial": "num1 = 5\nnum2 = 3\nresultado = # Completa aquí",
        "respuesta_esperada": 8,
        "tipo_comprobacion": "valor_exacto"
    },
    {
        "id": "multiplicacion_variable",
        "descripcion": "Multiplica la variable 'x' por 10 y guarda el resultado en 'y'. Si x = 7.",
        "codigo_inicial": "x = 7\ny = # Completa aquí",
        "respuesta_esperada": 70,
        "tipo_comprobacion": "valor_exacto"
    },
    {
        "id": "tipo_de_dato",
        "descripcion": "Usa la función 'type()' para obtener el tipo de dato de 15.5.",
        "codigo_inicial": "valor = 15.5\ntipo_valor = # Completa aquí",
        "respuesta_esperada": float, # Puedes usar el tipo directamente
        "tipo_comprobacion": "tipo_exacto"
    },
    {
        "id": "modulo_avanzado",
        "descripcion": "Calcula el resto de la división de 25 por 4.",
        "codigo_inicial": "resultado_modulo = # Completa aquí",
        "respuesta_esperada": 1,
        "tipo_comprobacion": "valor_exacto"
    },
    {
        "id": "funcion_suma",
        "descripcion": "Define una función llamada 'sumar_dos_numeros' que reciba dos argumentos y devuelva su suma.",
        "codigo_inicial": (
            "def sumar_dos_numeros(a, b):\n"
            "    # Tu código aquí\n"
            "    pass"
        ),
        "pruebas": [ # Para funciones, necesitas múltiples pruebas
            {"entradas": (2, 3), "salida_esperada": 5},
            {"entradas": (10, -5), "salida_esperada": 5},
            {"entradas": (0, 0), "salida_esperada": 0},
        ],
        "tipo_comprobacion": "funcion_tester"
    }
]