### Documento_punto(py)##
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AURELION MENÚ UNIFICADO
Combina el menú interactivo de documentación con el análisis de datos
Proyecto Tienda Aurelion - Demo 2
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import asyncio
import os

# ==========================================================
# DOCUMENTACIÓN DEL PROYECTO
# ==========================================================

textos_documentacion = {
    1: {
        "titulo": "1. Tema, problema y solución",
        "contenido": """
Este proyecto simula la gestión de la Tienda Aurelion utilizando datos sintéticos en Python, 
enfocándose en análisis de datos, visualización y modelado para un contexto de negocio minorista.

PROBLEMA:
La falta de escenarios prácticos y consistentes para aplicar técnicas de análisis de datos 
en entornos educativos, especialmente en simulaciones de tiendas con productos, clientes y ventas.

SOLUCIÓN:
Desarrollo de datasets sintéticos limpios (productos_demo2.csv, clientes_demo2.csv, 
detalle_ventas_demo2.csv) y un programa en Python con menú interactivo para explorar 
documentación y análisis. Incluye estadísticas descriptivas, distribuciones, correlaciones, 
detección de outliers y gráficos.
        """
    },
    2: {
        "titulo": "2. Dataset de referencia: Resumen de fuente y definición",
        "contenido": """
FUENTE: Datos generados con fines educativos.

DEFINICIÓN: Base de datos que representa una Tienda, con catálogo de productos, 
registro de clientes y operaciones de venta.

ARCHIVOS:
- productos_demo2.csv: ~100 productos con id, nombre, categoría y precio
- clientes_demo2.csv: ~100 clientes con id, nombre, email, ciudad y fecha_alta
- detalle_ventas_demo2.csv: ~343 ventas con id_venta, id_producto, cantidad, precio e importe
        """
    },
    3: {
        "titulo": "3. Estructura por tabla: Columnas, tipo y escala de medición",
        "contenido": """
PRODUCTOS (productos_demo2.csv) — ~100 filas
- id_producto: Entero (Ratio)
- nombre_producto: Texto (Nominal)
- categoria: Texto (Nominal) - 11 categorías
- precio_unitario: Decimal (Ratio)

CLIENTES (clientes_demo2.csv) — ~100 filas
- id_cliente: Entero (Ratio)
- nombre_cliente: Texto (Nominal)
- email: Texto (Nominal)
- ciudad: Texto (Nominal)
- fecha_alta: Fecha (Ordinal)

VENTAS (detalle_ventas_demo2.csv) — ~343 filas
- id_venta: Entero (Ratio)
- id_producto: Entero (Ratio)
- nombre_producto: Texto (Nominal)
- cantidad: Entero (Ratio)
- precio_unitario: Decimal (Ratio)
- importe: Decimal (Ratio)
        """
    },
    4: {
        "titulo": "4. Escalas de medición",
        "contenido": """
NOMINAL: Categoría, género, ubicación, nombre, email, ciudad
ORDINAL: Fecha (fecha_alta)
RATIO: Precio, stock, edad, cantidad, importe, id_producto, id_cliente, id_venta

Las escalas de medición permiten determinar qué tipo de análisis estadístico 
es apropiado para cada variable.
        """
    },
    5: {
        "titulo": "5. Sugerencias y mejoras con Copilot",
        "contenido": """
MEJORAS SUGERIDAS:
- Integrar machine learning para predicción de ventas
- Agregar más visualizaciones interactivas
- Implementar análisis de tendencias temporales
- Crear dashboard interactivo con gráficos dinámicos
- Análisis de segmentación de clientes
- Sistema de recomendaciones basado en compras previas
        """
    }
}

def obtener_contenido_completo():
    """Obtiene todo el contenido de la documentación como texto plano"""
    contenido = ""
    for seccion in textos_documentacion.values():
        contenido += seccion['titulo'] + "\n" + seccion['contenido'] + "\n\n"
    return contenido

# ==========================================================
# FUNCIONES DE ANÁLISIS DE DATOS
# ==========================================================

def cargar_datos():
    """Carga los datos desde los archivos CSV"""
    try:
        productos = pd.read_csv('productos_demo2.csv')
        clientes = pd.read_csv('clientes_demo2.csv')
        ventas = pd.read_csv('detalle_ventas_demo2.csv')
        
        # Función para categorizar productos
        def categorizar_producto(nombre):
            nombre_lower = nombre.lower()
            if any(palabra in nombre_lower for palabra in ['cerveza', 'fernet', 'gin', 'ron', 'vodka', 'whisky', 'vino', 'sidra', 'licor']):
                return 'Bebidas con Alcohol'
            if any(palabra in nombre_lower for palabra in ['coca cola', 'pepsi', 'sprite', 'fanta', 'agua mineral', 'jugo', 'energética', 'yerba mate', 'café', 'té']):
                return 'Bebidas sin Alcohol'
            if any(palabra in nombre_lower for palabra in ['leche', 'yogur', 'queso', 'manteca']):
                return 'Lácteos y Derivados'
            if any(palabra in nombre_lower for palabra in ['congelado', 'hamburguesa', 'empanada', 'pizza', 'precocido']):
                return 'Congelados y Precocinados'
            if any(palabra in nombre_lower for palabra in ['pan lactal', 'medialuna', 'bizcocho', 'galletita']):
                return 'Panadería y Repostería'
            if any(palabra in nombre_lower for palabra in ['mermelada', 'dulce de leche', 'miel']):
                return 'Untables, Mermeladas y Dulces'
            if any(palabra in nombre_lower for palabra in ['papas fritas', 'maní', 'mix de frutos secos', 'chocolate', 'barrita', 'caramelo', 'chicle', 'chupetín', 'alfajor', 'turrón']):
                return 'Golosinas, Snacks y Panificados'
            if any(palabra in nombre_lower for palabra in ['detergente', 'lavandina', 'desengrasante', 'limpiavidrios', 'suavizante', 'esponja', 'trapo', 'servilleta', 'papel higiénico']):
                return 'Limpieza del Hogar'
            if any(palabra in nombre_lower for palabra in ['shampoo', 'jabón', 'crema dental', 'cepillo', 'hilo dental', 'desodorante', 'toallas húmedas', 'mascarilla']):
                return 'Higiene Personal'
            if any(palabra in nombre_lower for palabra in ['arroz', 'fideo', 'lenteja', 'garbanzo', 'poroto', 'harina', 'azúcar', 'sal', 'aceite', 'vinagre', 'salsa de tomate', 'caldo', 'sopa instantánea', 'avena', 'granola', 'aceituna', 'stevia']):
                return 'Almacén y Despensa'
            if any(palabra in nombre_lower for palabra in ['helado']):
                return 'Otros Alimentos'
            return 'Otros Alimentos'
        
        # Aplicar categorización si no existe
        if 'categoria' not in productos.columns or productos['categoria'].isna().any():
            productos['categoria'] = productos['nombre_producto'].apply(categorizar_producto)
        
        # Preparar ventas con client_id y fecha
        np.random.seed(42)
        if 'client_id' not in ventas.columns:
            ventas['client_id'] = np.random.choice(clientes['id_cliente'].values, size=len(ventas))
        if 'fecha' not in ventas.columns:
            ventas['fecha'] = pd.date_range(start='2023-01-01', periods=len(ventas), freq='D')
        
        return productos, clientes, ventas
    except FileNotFoundError as e:
        print(f"Error: No se encontró el archivo {e.filename}")
        return None, None, None

def mostrar_datos(productos, clientes, ventas):
    """Muestra ejemplos de los datos cargados"""
    print("\n" + "="*60)
    print("EJEMPLOS DE DATOS")
    print("="*60)
    print("\n📦 PRODUCTOS (primeras 5 filas):")
    print(productos.head())
    print(f"\nTotal de productos: {len(productos)}")
    print(f"Categorías: {', '.join(sorted(productos['categoria'].unique()))}")
    
    print("\n👥 CLIENTES (primeras 5 filas):")
    print(clientes.head())
    print(f"\nTotal de clientes: {len(clientes)}")
    
    print("\n💰 VENTAS (primeras 5 filas):")
    print(ventas.head())
    print(f"\nTotal de ventas: {len(ventas)}")
    print(f"Importe total: ${ventas['importe'].sum():,.2f}")

def analisis_estadistico(productos, clientes, ventas):
    """Realiza análisis estadístico de los datos"""
    print("\n" + "="*60)
    print("ANÁLISIS ESTADÍSTICO")
    print("="*60)
    
    print("\n--- ESTADÍSTICAS DESCRIPTIVAS DE VENTAS ---")
    print(ventas[['cantidad', 'precio_unitario', 'importe']].describe())
    
    print("\n--- ESTADÍSTICAS DE PRODUCTOS ---")
    print(f"Precio promedio: ${productos['precio_unitario'].mean():,.2f}")
    print(f"Precio mínimo: ${productos['precio_unitario'].min():,.2f}")
    print(f"Precio máximo: ${productos['precio_unitario'].max():,.2f}")
    
    print("\n--- ANÁLISIS POR CATEGORÍA ---")
    ventas_con_cat = ventas.merge(productos[['id_producto', 'categoria']], on='id_producto', how='left')
    ventas_por_categoria = ventas_con_cat.groupby('categoria')['importe'].agg(['sum', 'mean', 'count'])
    ventas_por_categoria.columns = ['Total', 'Promedio', 'Cantidad_Ventas']
    print(ventas_por_categoria.sort_values('Total', ascending=False))
    
    # Detección de outliers
    Q1 = ventas['importe'].quantile(0.25)
    Q3 = ventas['importe'].quantile(0.75)
    IQR = Q3 - Q1
    outliers = ventas[(ventas['importe'] < Q1 - 1.5 * IQR) | (ventas['importe'] > Q3 + 1.5 * IQR)]
    print(f"\n--- OUTLIERS DETECTADOS ---")
    print(f"Total de outliers: {len(outliers)} ({len(outliers)/len(ventas)*100:.2f}%)")

def mostrar_graficos(productos, clientes, ventas):
    """Muestra gráficos básicos de análisis"""
    print("\n" + "="*60)
    print("GENERANDO GRÁFICOS...")
    print("="*60)
    
    # Gráfico 1: Distribución de precios
    plt.figure(figsize=(10, 6))
    plt.hist(productos['precio_unitario'], bins=20, edgecolor='black', alpha=0.7)
    plt.title('Distribución de Precios de Productos', fontsize=14, fontweight='bold')
    plt.xlabel('Precio ($)', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafico_distribucion_precios.png', dpi=150, bbox_inches='tight')
    print("✓ Gráfico guardado: grafico_distribucion_precios.png")
    plt.close()
    
    # Gráfico 2: Ventas por categoría
    ventas_con_cat = ventas.merge(productos[['id_producto', 'categoria']], on='id_producto', how='left')
    ventas_por_cat = ventas_con_cat.groupby('categoria')['importe'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(12, 6))
    ventas_por_cat.plot(kind='bar', color='steelblue', edgecolor='navy', alpha=0.7)
    plt.title('Ventas Totales por Categoría', fontsize=14, fontweight='bold')
    plt.xlabel('Categoría', fontsize=12)
    plt.ylabel('Ventas ($)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafico_ventas_por_categoria.png', dpi=150, bbox_inches='tight')
    print("✓ Gráfico guardado: grafico_ventas_por_categoria.png")
    plt.close()
    
    # Gráfico 3: Correlación precio vs cantidad
    plt.figure(figsize=(10, 6))
    plt.scatter(ventas['precio_unitario'], ventas['cantidad'], alpha=0.6, s=50)
    plt.title('Correlación Precio vs Cantidad Vendida', fontsize=14, fontweight='bold')
    plt.xlabel('Precio Unitario ($)', fontsize=12)
    plt.ylabel('Cantidad', fontsize=12)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafico_correlacion_precio_cantidad.png', dpi=150, bbox_inches='tight')
    print("✓ Gráfico guardado: grafico_correlacion_precio_cantidad.png")
    plt.close()
    
    print("\n✅ Todos los gráficos generados exitosamente")

# ==========================================================
# MENÚ DE DOCUMENTACIÓN (ASÍNCRONO)
# ==========================================================

async def mostrar_menu_documentacion():
    """Muestra el menú de documentación"""
    print("\n" + "="*60)
    print("MENÚ DE DOCUMENTACIÓN DEL PROYECTO TIENDA AURELION")
    print("="*60)
    print("1. Tema, problema y solución")
    print("2. Dataset de referencia")
    print("3. Estructura por tabla (tipo y escala)")
    print("4. Escalas de medición")
    print("5. Sugerencias y mejoras con Copilot")
    print("6. Volver al menú principal")
    print("7. Búsqueda (palabras clave)")
    print("8. Exportar sección actual")

async def procesar_opcion_documentacion(opcion, seccion_actual=None):
    """Procesa las opciones del menú de documentación"""
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
        return None  # Volver al menú principal
    elif opcion == 7:  # Búsqueda
        palabra = input("Ingrese palabra clave para buscar: ").lower()
        contenido_completo = obtener_contenido_completo().lower()
        if palabra in contenido_completo:
            print(f"\nPalabra '{palabra}' encontrada. Resultados:\n")
            for num, seccion in textos_documentacion.items():
                if palabra in seccion["contenido"].lower():
                    print(f"  • Sección {num}: {seccion['titulo']}")
        else:
            print(f"Palabra '{palabra}' no encontrada.")
        return seccion_actual
    elif opcion == 8:  # Exportar
        if seccion_actual and seccion_actual in textos_documentacion:
            nombre_archivo = f"seccion_{seccion_actual}.txt"
            with open(nombre_archivo, "w", encoding='utf-8') as f:
                f.write(f"{textos_documentacion[seccion_actual]['titulo']}\n{textos_documentacion[seccion_actual]['contenido']}")
            print(f"✓ Sección exportada a {nombre_archivo}")
        else:
            print("No hay sección actual para exportar.")
        return seccion_actual
    else:
        print("Opción inválida. Intente de nuevo.")
        return seccion_actual

async def menu_documentacion():
    """Menú asincrónico de documentación"""
    seccion_actual = None
    while True:
        await mostrar_menu_documentacion()
        try:
            opcion = int(input("\nSeleccione una opción: "))
            seccion_actual = await procesar_opcion_documentacion(opcion, seccion_actual)
            if seccion_actual is None:
                break
            input("\nPresione Enter para continuar...")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
        except KeyboardInterrupt:
            print("\n\nSaliendo...")
            break

# ==========================================================
# MENÚ PRINCIPAL
# ==========================================================

def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("AURELION - MENÚ PRINCIPAL")
    print("="*60)
    print("1. Ver ejemplos de datos")
    print("2. Realizar análisis estadístico")
    print("3. Mostrar gráficos")
    print("4. Documentación del proyecto")
    print("5. Generar gráficos completos (ejecutar_graficos.py)")
    print("6. Generar presentación HTML del proyecto")
    print("7. Salir")
    print("="*60)

def menu_principal():
    """Menú principal del programa"""
    productos, clientes, ventas = cargar_datos()
    
    if productos is None:
        print("Error: No se pudieron cargar los datos. Verifique que los archivos CSV existan.")
        return
    
    while True:
        mostrar_menu_principal()
        try:
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == '1':
                mostrar_datos(productos, clientes, ventas)
                input("\nPresione Enter para continuar...")
            elif opcion == '2':
                analisis_estadistico(productos, clientes, ventas)
                input("\nPresione Enter para continuar...")
            elif opcion == '3':
                mostrar_graficos(productos, clientes, ventas)
                input("\nPresione Enter para continuar...")
            elif opcion == '4':
                asyncio.run(menu_documentacion())
            elif opcion == '5':
                print("\n" + "="*60)
                print("GENERANDO GRÁFICOS COMPLETOS...")
                print("="*60)
                if os.path.exists('ejecutar_graficos.py'):
                    os.system('python ejecutar_graficos.py')
                else:
                    print("Error: No se encontró el archivo ejecutar_graficos.py")
                input("\nPresione Enter para continuar...")
            elif opcion == '6':
                print("\n" + "="*60)
                print("GENERANDO PRESENTACIÓN HTML...")
                print("="*60)
                if os.path.exists('generar_presentacion.py'):
                    os.system('python generar_presentacion.py')
                    print("\n✅ Presentación generada: presentacion_aurelion.html")
                    print("💡 Abre el archivo en tu navegador para ver la presentación")
                else:
                    print("Error: No se encontró el archivo generar_presentacion.py")
                input("\nPresione Enter para continuar...")
            elif opcion == '7':
                print("\n¡Gracias por usar Aurelion Demo 2! ¡Hasta pronto!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except KeyboardInterrupt:
            print("\n\nSaliendo del programa...")
            break
        except Exception as e:
            print(f"Error: {e}")
            input("\nPresione Enter para continuar...")

# ==========================================================
# PUNTO DE ENTRADA
# ==========================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("BIENVENIDO A AURELION DEMO 2")
    print("Sistema de Gestión y Análisis de Tienda")
    print("="*60)
    menu_principal()

