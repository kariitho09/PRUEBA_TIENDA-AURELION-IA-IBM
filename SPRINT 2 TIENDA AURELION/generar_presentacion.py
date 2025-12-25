#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERADOR DE PRESENTACIÓN DEL PROYECTO AURELION
Crea una presentación HTML interactiva con toda la información y gráficos del proyecto
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime
import base64

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
        
        if 'categoria' not in productos.columns or productos['categoria'].isna().any():
            productos['categoria'] = productos['nombre_producto'].apply(categorizar_producto)
        
        np.random.seed(42)
        if 'client_id' not in ventas.columns:
            ventas['client_id'] = np.random.choice(clientes['id_cliente'].values, size=len(ventas))
        if 'fecha' not in ventas.columns:
            ventas['fecha'] = pd.date_range(start='2023-01-01', periods=len(ventas), freq='D')
        
        return productos, clientes, ventas
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return None, None, None

def imagen_a_base64(ruta_imagen):
    """Convierte una imagen a base64 para incrustarla en HTML"""
    try:
        with open(ruta_imagen, 'rb') as img_file:
            img_data = img_file.read()
            img_base64 = base64.b64encode(img_data).decode('utf-8')
            ext = os.path.splitext(ruta_imagen)[1][1:].lower()
            return f"data:image/{ext};base64,{img_base64}"
    except:
        return None

def obtener_estadisticas(productos, clientes, ventas):
    """Obtiene estadísticas del proyecto"""
    ventas_con_cat = ventas.merge(productos[['id_producto', 'categoria']], on='id_producto', how='left')
    ventas_por_categoria = ventas_con_cat.groupby('categoria')['importe'].sum().sort_values(ascending=False)
    
    stats = {
        'total_productos': len(productos),
        'total_clientes': len(clientes),
        'total_ventas': len(ventas),
        'importe_total': ventas['importe'].sum(),
        'importe_promedio': ventas['importe'].mean(),
        'categoria_top': ventas_por_categoria.index[0],
        'ventas_categoria_top': ventas_por_categoria.iloc[0],
        'categorias': len(productos['categoria'].unique()),
        'precio_promedio': productos['precio_unitario'].mean(),
        'precio_min': productos['precio_unitario'].min(),
        'precio_max': productos['precio_unitario'].max(),
    }
    return stats, ventas_por_categoria

def generar_html_presentacion():
    """Genera la presentación HTML completa"""
    print("📊 Cargando datos...")
    productos, clientes, ventas = cargar_datos()
    
    if productos is None:
        print("Error: No se pudieron cargar los datos")
        return
    
    print("📈 Calculando estadísticas...")
    stats, ventas_por_categoria = obtener_estadisticas(productos, clientes, ventas)
    
    print("🖼️  Cargando gráficos...")
    graficos = {
        'grafico1': 'grafico1_ventas_por_cliente.png',
        'grafico2': 'grafico2_ventas_vs_crecimiento.png',
        'grafico3': 'grafico3_comparacion_tradicional_vs_ia.png',
        'grafico4': 'grafico4_heatmap_ventas_mes_categoria.png'
    }
    
    graficos_base64 = {}
    for nombre, archivo in graficos.items():
        if os.path.exists(archivo):
            graficos_base64[nombre] = imagen_a_base64(archivo)
        else:
            graficos_base64[nombre] = None
    
    # Generar tabla de categorías
    tabla_categorias = ""
    for i, (categoria, total) in enumerate(ventas_por_categoria.items(), 1):
        porcentaje = (total / stats['importe_total']) * 100
        tabla_categorias += f"""
        <tr>
            <td>{i}</td>
            <td>{categoria}</td>
            <td>${total:,.2f}</td>
            <td>{porcentaje:.1f}%</td>
        </tr>
        """
    
    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Presentación Proyecto Aurelion</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        .slide {{
            background: white;
            border-radius: 15px;
            padding: 40px;
            margin: 30px 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            animation: fadeIn 0.5s ease-in;
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        h1 {{
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 20px;
            text-align: center;
            border-bottom: 3px solid #667eea;
            padding-bottom: 15px;
        }}
        
        h2 {{
            color: #764ba2;
            font-size: 2em;
            margin: 30px 0 20px 0;
            border-left: 5px solid #764ba2;
            padding-left: 15px;
        }}
        
        h3 {{
            color: #667eea;
            font-size: 1.5em;
            margin: 20px 0 10px 0;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}
        
        .stat-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            transition: transform 0.3s;
        }}
        
        .stat-card:hover {{
            transform: translateY(-5px);
        }}
        
        .stat-card h3 {{
            color: white;
            font-size: 1.2em;
            margin-bottom: 10px;
        }}
        
        .stat-card .value {{
            font-size: 2em;
            font-weight: bold;
            margin-top: 10px;
        }}
        
        .grafico-container {{
            text-align: center;
            margin: 30px 0;
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
        }}
        
        .grafico-container img {{
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        
        .grafico-container h3 {{
            margin-bottom: 20px;
            color: #333;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        th, td {{
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        
        th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: bold;
        }}
        
        tr:hover {{
            background: #f5f5f5;
        }}
        
        .info-box {{
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        
        .footer {{
            text-align: center;
            padding: 20px;
            color: white;
            margin-top: 40px;
        }}
        
        .nav-buttons {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            display: flex;
            gap: 10px;
        }}
        
        .nav-btn {{
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.2);
        }}
        
        .nav-btn:hover {{
            background: #764ba2;
        }}
        
        @media print {{
            .nav-buttons {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Slide 1: Portada -->
        <div class="slide">
            <h1>🏪 PROYECTO AURELION</h1>
            <h2 style="text-align: center; border: none; padding: 0; margin: 20px 0;">
                Sistema de Gestión y Análisis de Tienda
            </h2>
            <div class="info-box" style="text-align: center; margin: 40px 0;">
                <p style="font-size: 1.2em; margin: 10px 0;">
                    <strong>Análisis de Datos, Visualización y Modelado</strong>
                </p>
                <p style="margin-top: 20px; color: #666;">
                    Generado el {fecha_actual}
                </p>
            </div>
        </div>
        
        <!-- Slide 2: Información del Proyecto -->
        <div class="slide">
            <h2>📋 Información del Proyecto</h2>
            <div class="info-box">
                <h3>Tema</h3>
                <p>Este proyecto simula la gestión de la Tienda Aurelion utilizando datos sintéticos en Python, 
                enfocándose en análisis de datos, visualización y modelado para un contexto de negocio minorista.</p>
            </div>
            <div class="info-box">
                <h3>Problema</h3>
                <p>La falta de escenarios prácticos y consistentes para aplicar técnicas de análisis de datos 
                en entornos educativos, especialmente en simulaciones de tiendas con productos, clientes y ventas.</p>
            </div>
            <div class="info-box">
                <h3>Solución</h3>
                <p>Desarrollo de datasets sintéticos limpios (productos_demo2.csv, clientes_demo2.csv, 
                detalle_ventas_demo2.csv) y un programa en Python con menú interactivo para explorar 
                documentación y análisis. Incluye estadísticas descriptivas, distribuciones, correlaciones, 
                detección de outliers y gráficos.</p>
            </div>
        </div>
        
        <!-- Slide 3: Estadísticas Generales -->
        <div class="slide">
            <h2>📊 Estadísticas Generales</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <h3>Total de Productos</h3>
                    <div class="value">{stats['total_productos']}</div>
                </div>
                <div class="stat-card">
                    <h3>Total de Clientes</h3>
                    <div class="value">{stats['total_clientes']}</div>
                </div>
                <div class="stat-card">
                    <h3>Total de Ventas</h3>
                    <div class="value">{stats['total_ventas']}</div>
                </div>
                <div class="stat-card">
                    <h3>Importe Total</h3>
                    <div class="value">${stats['importe_total']:,.0f}</div>
                </div>
                <div class="stat-card">
                    <h3>Importe Promedio</h3>
                    <div class="value">${stats['importe_promedio']:,.0f}</div>
                </div>
                <div class="stat-card">
                    <h3>Categorías</h3>
                    <div class="value">{stats['categorias']}</div>
                </div>
            </div>
        </div>
        
        <!-- Slide 4: Ventas por Categoría -->
        <div class="slide">
            <h2>📦 Ventas por Categoría</h2>
            <table>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Categoría</th>
                        <th>Ventas Totales</th>
                        <th>Porcentaje</th>
                    </tr>
                </thead>
                <tbody>
                    {tabla_categorias}
                </tbody>
            </table>
            <div class="info-box" style="margin-top: 20px;">
                <p><strong>Categoría más vendida:</strong> {stats['categoria_top']} 
                (${stats['ventas_categoria_top']:,.2f})</p>
            </div>
        </div>
        
        <!-- Slide 5: Gráfico 1 - Ventas por Cliente -->
        <div class="slide">
            <h2>📈 Gráfico 1: Ventas por Cliente</h2>
            <div class="grafico-container">
                <h3>Top 20 Clientes por Ventas Totales</h3>
                {"<img src='" + graficos_base64['grafico1'] + "' alt='Ventas por Cliente'>" if graficos_base64['grafico1'] else "<p style='color: red;'>Gráfico no disponible</p>"}
            </div>
            <div class="info-box">
                <p>Este gráfico muestra los 20 clientes con mayores ventas, permitiendo identificar 
                los clientes más valiosos para la tienda.</p>
            </div>
        </div>
        
        <!-- Slide 6: Gráfico 2 - Ventas vs Crecimiento -->
        <div class="slide">
            <h2>📈 Gráfico 2: Ventas vs Crecimiento Proyectado</h2>
            <div class="grafico-container">
                <h3>Relación entre Ventas Actuales y Crecimiento Futuro</h3>
                {"<img src='" + graficos_base64['grafico2'] + "' alt='Ventas vs Crecimiento'>" if graficos_base64['grafico2'] else "<p style='color: red;'>Gráfico no disponible</p>"}
            </div>
            <div class="info-box">
                <p>Visualiza la relación entre el volumen de ventas actual y el potencial de crecimiento futuro, 
                ayudando a identificar oportunidades de expansión.</p>
            </div>
        </div>
        
        <!-- Slide 7: Gráfico 3 - Comparación Tradicional vs IA -->
        <div class="slide">
            <h2>🤖 Gráfico 3: Sistema Tradicional vs Sistema con IA</h2>
            <div class="grafico-container">
                <h3>Comparación de Crecimiento Proyectado</h3>
                {"<img src='" + graficos_base64['grafico3'] + "' alt='Comparación Tradicional vs IA'>" if graficos_base64['grafico3'] else "<p style='color: red;'>Gráfico no disponible</p>"}
            </div>
            <div class="info-box">
                <p>Demuestra el crecimiento histórico y proyectado comparando un sistema tradicional de marketing/ventas 
                con uno potenciado por Inteligencia Artificial, mostrando claramente las ventajas competitivas del sistema con IA.</p>
            </div>
        </div>
        
        <!-- Slide 8: Gráfico 4 - HeatMap -->
        <div class="slide">
            <h2>🔥 Gráfico 4: HeatMap de Ventas por Mes y Categoría</h2>
            <div class="grafico-container">
                <h3>Análisis Temporal de Ventas por Categoría</h3>
                {"<img src='" + graficos_base64['grafico4'] + "' alt='HeatMap Ventas'>" if graficos_base64['grafico4'] else "<p style='color: red;'>Gráfico no disponible</p>"}
            </div>
            <div class="info-box">
                <p>Visualiza las ventas por mes y categoría de producto, permitiendo identificar qué categorías de productos 
                se venden más en cada mes, patrones temporales y tendencias de ventas por categoría a lo largo del tiempo.</p>
            </div>
        </div>
        
        <!-- Slide 9: Análisis de Precios -->
        <div class="slide">
            <h2>💰 Análisis de Precios</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <h3>Precio Promedio</h3>
                    <div class="value">${stats['precio_promedio']:,.2f}</div>
                </div>
                <div class="stat-card">
                    <h3>Precio Mínimo</h3>
                    <div class="value">${stats['precio_min']:,.2f}</div>
                </div>
                <div class="stat-card">
                    <h3>Precio Máximo</h3>
                    <div class="value">${stats['precio_max']:,.2f}</div>
                </div>
            </div>
        </div>
        
        <!-- Slide 10: Conclusiones -->
        <div class="slide">
            <h2>🎯 Conclusiones y Mejoras Futuras</h2>
            <div class="info-box">
                <h3>Insights Principales</h3>
                <ul style="margin-left: 20px; margin-top: 10px;">
                    <li>La categoría <strong>{stats['categoria_top']}</strong> representa la mayor fuente de ingresos</li>
                    <li>El sistema con IA muestra un crecimiento significativamente mayor que el tradicional</li>
                    <li>Existen patrones temporales claros en las ventas por categoría</li>
                    <li>Los clientes top representan una porción importante de las ventas totales</li>
                </ul>
            </div>
            <div class="info-box" style="margin-top: 20px;">
                <h3>Mejoras Sugeridas</h3>
                <ul style="margin-left: 20px; margin-top: 10px;">
                    <li>Integrar machine learning para predicción de ventas</li>
                    <li>Agregar más visualizaciones interactivas</li>
                    <li>Implementar análisis de tendencias temporales avanzadas</li>
                    <li>Crear dashboard interactivo con gráficos dinámicos</li>
                    <li>Análisis de segmentación de clientes</li>
                    <li>Sistema de recomendaciones basado en compras previas</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>Proyecto Aurelion - Sistema de Gestión y Análisis de Tienda</p>
        <p>Generado el {fecha_actual}</p>
    </div>
    
    <div class="nav-buttons">
        <button class="nav-btn" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">↑ Inicio</button>
        <button class="nav-btn" onclick="window.print()">🖨️ Imprimir</button>
    </div>
</body>
</html>
    """
    
    # Guardar el archivo HTML
    nombre_archivo = 'presentacion_aurelion.html'
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"\n✅ Presentación generada exitosamente: {nombre_archivo}")
    print(f"📂 Abre el archivo en tu navegador para ver la presentación")
    return nombre_archivo

if __name__ == "__main__":
    print("="*60)
    print("GENERADOR DE PRESENTACIÓN - PROYECTO AURELION")
    print("="*60)
    archivo = generar_html_presentacion()
    if archivo:
        print(f"\n💡 Para abrir la presentación, ejecuta:")
        print(f"   - En Linux/Mac: xdg-open {archivo} o open {archivo}")
        print(f"   - En Windows: start {archivo}")
        print(f"   - O simplemente abre {archivo} con tu navegador")

