# corrector.py
import io
import contextlib

def verificar_ejercicio(ejercicio, codigo_usuario):
    """
    Verifica la solución de un ejercicio dado el código del usuario.
    Retorna un diccionario con el resultado de la corrección.
    """
    id_ejercicio = ejercicio["id"]
    descripcion = ejercicio["descripcion"]
    tipo_comprobacion = ejercicio["tipo_comprobacion"]
    respuesta_esperada = ejercicio.get("respuesta_esperada") # Usamos .get() por si no existe
    pruebas = ejercicio.get("pruebas")

    print(f"\n--- Corrigiendo ejercicio: '{id_ejercicio}' ---")
    print(f"Descripción: {descripcion}")

    try:
        # Ejecutar el código del usuario en un entorno aislado
        # Usamos un diccionario para el scope y capturamos la salida
        local_scope = {}
        output_buffer = io.StringIO()

        with contextlib.redirect_stdout(output_buffer):
            exec(codigo_usuario, {}, local_scope) # {} para globals, local_scope para locals

        salida_consola_usuario = output_buffer.getvalue().strip()
        print(f"Código del usuario ejecutado. Variables locales: {local_scope}")


        if tipo_comprobacion == "valor_exacto":
            # Extraer la variable que contiene la respuesta (asumiendo que es 'resultado' o 'y', etc.)
            # Aquí necesitas una forma de saber qué variable buscar.
            # Podrías añadir al ejercicio un "variable_a_verificar": "resultado"
            # Por simplicidad, asumamos que es la última variable creada o una específica.
            # Esto es un punto donde puedes mejorar la robustez.

            # Una forma simple (pero no infalible) es buscar la variable definida en el código
            # o pedir al usuario que guarde en una variable específica (e.g., 'mi_respuesta')
            
            # Para este ejemplo, intentaremos obtener 'resultado' o 'y' o 'resultado_modulo'
            # del scope local.
            variable_a_verificar = None
            if "resultado" in local_scope:
                variable_a_verificar = local_scope["resultado"]
            elif "y" in local_scope:
                variable_a_verificar = local_scope["y"]
            elif "tipo_valor" in local_scope:
                variable_a_verificar = local_scope["tipo_valor"]
            elif "resultado_modulo" in local_scope:
                variable_a_verificar = local_scope["resultado_modulo"]
            else:
                return {
                    "id": id_ejercicio,
                    "aprobado": False,
                    "mensaje": "Error: No se encontró la variable esperada con la respuesta en tu código.",
                    "detalles": f"Variables disponibles: {list(local_scope.keys())}"
                }


            if variable_a_verificar == respuesta_esperada:
                return {
                    "id": id_ejercicio,
                    "aprobado": True,
                    "mensaje": "¡Correcto! El valor es el esperado."
                }
            else:
                return {
                    "id": id_ejercicio,
                    "aprobado": False,
                    "mensaje": "Incorrecto. El valor obtenido no es el esperado.",
                    "detalles": f"Obtenido: {variable_a_verificar}, Esperado: {respuesta_esperada}"
                }

        elif tipo_comprobacion == "tipo_exacto":
            variable_a_verificar = None
            if "tipo_valor" in local_scope: # Asumimos que la variable es 'tipo_valor'
                variable_a_verificar = local_scope["tipo_valor"]
            else:
                return {
                    "id": id_ejercicio,
                    "aprobado": False,
                    "mensaje": "Error: No se encontró la variable 'tipo_valor' en tu código.",
                    "detalles": f"Variables disponibles: {list(local_scope.keys())}"
                }

            if variable_a_verificar == respuesta_esperada:
                return {
                    "id": id_ejercicio,
                    "aprobado": True,
                    "mensaje": "¡Correcto! El tipo de dato es el esperado."
                }
            else:
                return {
                    "id": id_ejercicio,
                    "aprobado": False,
                    "mensaje": "Incorrecto. El tipo de dato obtenido no es el esperado.",
                    "detalles": f"Obtenido: {variable_a_verificar}, Esperado: {respuesta_esperada}"
                }

        elif tipo_comprobacion == "funcion_tester":
            if "sumar_dos_numeros" not in local_scope or not callable(local_scope["sumar_dos_numeros"]):
                return {
                    "id": id_ejercicio,
                    "aprobado": False,
                    "mensaje": "Error: La función 'sumar_dos_numeros' no fue definida correctamente.",
                    "detalles": f"Funciones/variables disponibles: {list(local_scope.keys())}"
                }

            funcion_usuario = local_scope["sumar_dos_numeros"]
            todas_las_pruebas_pasaron = True
            fallos_detalles = []

            for i, prueba in enumerate(pruebas):
                entradas = prueba["entradas"]
                salida_esperada = prueba["salida_esperada"]
                try:
                    salida_obtenida = funcion_usuario(*entradas) # Desempaqueta las entradas
                    if salida_obtenida != salida_esperada:
                        todas_las_pruebas_pasaron = False
                        fallos_detalles.append(f"Prueba {i+1} fallida: Entrada {entradas}, Esperado {salida_esperada}, Obtenido {salida_obtenida}")
                except Exception as e:
                    todas_las_pruebas_pasaron = False
                    fallos_detalles.append(f"Prueba {i+1} fallida por excepción: {e}")

            if todas_las_pruebas_pasaron:
                return {
                    "id": id_ejercicio,
                    "aprobado": True,
                    "mensaje": "¡Correcto! Todas las pruebas para la función pasaron."
                }
            else:
                return {
                    "id": id_ejercicio,
                    "aprobado": False,
                    "mensaje": "Algunas pruebas para la función fallaron.",
                    "detalles": fallos_detalles
                }

        else:
            return {
                "id": id_ejercicio,
                "aprobado": False,
                "mensaje": "Tipo de comprobación no soportado."
            }

    except SyntaxError as e:
        return {
            "id": id_ejercicio,
            "aprobado": False,
            "mensaje": "Error de sintaxis en tu código.",
            "detalles": str(e)
        }
    except NameError as e:
        return {
            "id": id_ejercicio,
            "aprobado": False,
            "mensaje": "Error de nombre (variable no definida) en tu código.",
            "detalles": str(e)
        }
    except Exception as e:
        return {
            "id": id_ejercicio,
            "aprobado": False,
            "mensaje": "Ocurrió un error inesperado al ejecutar tu código.",
            "detalles": str(e)
        }