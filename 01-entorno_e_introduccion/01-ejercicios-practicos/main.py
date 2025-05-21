# main.py
import os
from ejercicios import ejercicios_disponibles
from corrector import verificar_ejercicio

def limpiar_pantalla():
    # Para limpiar la consola (funciona en la mayoría de sistemas)
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_ejercicio(ejercicio):
    print("\n" + "="*50)
    print(f"EJERCICIO: {ejercicio['id'].replace('_', ' ').upper()}")
    print("="*50)
    print(f"Descripción:\n{ejercicio['descripcion']}\n")
    print("--- Escribe tu código a continuación. Presiona Enter y luego Ctrl+D (o Ctrl+Z en Windows) para terminar. ---")
    if ejercicio.get("codigo_inicial"):
        print("\nCódigo inicial (puedes copiarlo y modificarlo):")
        print("```python") # Bloque de código Markdown para VS Code
        print(ejercicio["codigo_inicial"])
        print("```")
    print("\nTu código:")


def obtener_codigo_usuario():
    """Lee múltiples líneas de entrada del usuario hasta que termina."""
    lineas = []
    while True:
        try:
            linea = input()
            lineas.append(linea)
        except EOFError: # Se activa con Ctrl+D (Linux/macOS) o Ctrl+Z + Enter (Windows)
            break
    return "\n".join(lineas)

def ejecutar_ejercicios():
    limpiar_pantalla()
    print("¡Bienvenido al sistema de ejercicios de Python!")
    print("Vamos a practicar algunas operaciones y conceptos básicos.")

    for i, ejercicio in enumerate(ejercicios_disponibles):
        mostrar_ejercicio(ejercicio)
        codigo_usuario = obtener_codigo_usuario()
        limpiar_pantalla() # Limpia la pantalla antes de mostrar el feedback

        print("Analizando tu código...")
        feedback = verificar_ejercicio(ejercicio, codigo_usuario)

        print("\n--- RESULTADO ---")
        if feedback["aprobado"]:
            print(f"✅ ¡EJERCICIO '{ejercicio['id']}' APROBADO!")
        else:
            print(f"❌ EJERCICIO '{ejercicio['id']}' FALLIDO.")
        print(f"Mensaje: {feedback['mensaje']}")
        if "detalles" in feedback:
            print("Detalles:")
            if isinstance(feedback["detalles"], list):
                for detalle in feedback["detalles"]:
                    print(f"  - {detalle}")
            else:
                print(f"  - {feedback['detalles']}")
        
        input("\nPresiona Enter para continuar con el siguiente ejercicio...")
        limpiar_pantalla()

    print("\n¡Has completado todos los ejercicios!")
    print("¡Sigue practicando!")

if __name__ == "__main__":
    ejecutar_ejercicios()