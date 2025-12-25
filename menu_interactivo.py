
### 2. `main.py` (Código principal del menú asincrónico)
```python
# main.py: Visor interactivo asincrónico de la documentación.

import asyncio
from textos import textos_documentacion, obtener_contenido_completo

async def mostrar_menu():
    print("\n=== Menú de Documentación del Proyecto Tienda ===")
    print("1. Tema, problema y solución")
    print("2. Dataset de referencia")
    print("3. Estructura por tabla (tipo y escala)")
    print("4. Escalas de medición")
    print("5. Sugerencias y mejoras con Copilot")
    print("6. Salir")
    print("7. Búsqueda (palabras clave)")  # Mejora aplicada
    print("8. Exportar sección actual")   # Mejora aplicada

async def procesar_opcion(opcion, seccion_actual=None):
    if opcion == 1:
        seccion = textos_documentacion[1]
        print(f"\n{seccion['titulo']}\n{seccion['contenido']}")
        return 1
    elif opcion == 2:
        seccion = textos_documentacion[2]
        print(f"\n{seccion['titulo']}\n{seccion['contenido']}")
        return 2
    elif opcion == 3:
        seccion = textos_documentacion[3]
        print(f"\n{seccion['titulo']}\n{seccion['contenido']}")
        return 3
    elif opcion == 4:
        seccion = textos_documentacion[4]
        print(f"\n{seccion['titulo']}\n{seccion['contenido']}")
        return 4
    elif opcion == 5:
        seccion = textos_documentacion[5]
        print(f"\n{seccion['titulo']}\n{seccion['contenido']}")
        return 5
    elif opcion == 6:
        print("Saliendo del programa...")
        return None
    elif opcion == 7:  # Búsqueda
        palabra = input("Ingrese palabra clave para buscar: ").lower()
        contenido_completo = obtener_contenido_completo().lower()
        if palabra in contenido_completo:
            print(f"Palabra '{palabra}' encontrada. Resultados:\n")
            for num, seccion in textos_documentacion.items():
                if palabra in seccion["contenido"].lower():
                    print(f"Sección {num}: {seccion['titulo']}")
        else:
            print(f"Palabra '{palabra}' no encontrada.")
        return seccion_actual  # Mantener sección actual
    elif opcion == 8:  # Exportar
        if seccion_actual and seccion_actual in textos_documentacion:
            nombre_archivo = f"seccion_{seccion_actual}.txt"
            with open(nombre_archivo, "w") as f:
                f.write(f"{textos_documentacion[seccion_actual]['titulo']}\n{textos_documentacion[seccion_actual]['contenido']}")
            print(f"Sección exportada a {nombre_archivo}")
        else:
            print("No hay sección actual para exportar.")
        return seccion_actual
    else:
        print("Opción inválida. Intente de nuevo.")
        return seccion_actual

async def main():
    seccion_actual = None
    while True:
        await mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            seccion_actual = await procesar_opcion(opcion, seccion_actual)
            if seccion_actual is None:
                break
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

if __name__ == "__main__":
    asyncio.run(main())