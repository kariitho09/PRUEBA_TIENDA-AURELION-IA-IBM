#!/usr/bin/env python3
# Script para ejecutar el código del notebook y generar los gráficos

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import os

# Configuración de estilo (compatible con diferentes versiones)
try:
    plt.style.use('seaborn-v0_8-darkgrid')
except:
    try:
        plt.style.use('seaborn-darkgrid')
    except:
        plt.style.use('ggplot')

sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

print("=" * 60)
print("ANÁLISIS DE VENTAS Y PROYECCIONES - TIENDA AURELION")
print("=" * 60)
print("\n✓ Librerías importadas correctamente\n")

# ============================================================
# CELDA 1: Cargar datos
# ============================================================
print("📊 Cargando datos...")
productos = pd.read_csv('productos_demo2.csv')
clientes = pd.read_csv('clientes_demo2.csv')
ventas = pd.read_csv('detalle_ventas_demo2.csv')

# Función para categorizar productos según su nombre
def categorizar_producto(nombre):
    nombre_lower = nombre.lower()
    
    # Bebidas con Alcohol
    if any(palabra in nombre_lower for palabra in ['cerveza', 'fernet', 'gin', 'ron', 'vodka', 'whisky', 'vino', 'sidra', 'licor']):
        return 'Bebidas con Alcohol'
    
    # Bebidas sin Alcohol
    if any(palabra in nombre_lower for palabra in ['coca cola', 'pepsi', 'sprite', 'fanta', 'agua mineral', 'jugo', 'energética', 'yerba mate', 'café', 'té']):
        return 'Bebidas sin Alcohol'
    
    # Lácteos y Derivados
    if any(palabra in nombre_lower for palabra in ['leche', 'yogur', 'queso', 'manteca']):
        return 'Lácteos y Derivados'
    
    # Congelados y Precocinados
    if any(palabra in nombre_lower for palabra in ['congelado', 'hamburguesa', 'empanada', 'pizza', 'precocido']):
        return 'Congelados y Precocinados'
    
    # Panadería y Repostería
    if any(palabra in nombre_lower for palabra in ['pan lactal', 'medialuna', 'bizcocho', 'galletita']):
        return 'Panadería y Repostería'
    
    # Untables, Mermeladas y Dulces
    if any(palabra in nombre_lower for palabra in ['mermelada', 'dulce de leche', 'miel']):
        return 'Untables, Mermeladas y Dulces'
    
    # Golosinas, Snacks y Panificados
    if any(palabra in nombre_lower for palabra in ['papas fritas', 'maní', 'mix de frutos secos', 'chocolate', 'barrita', 'caramelo', 'chicle', 'chupetín', 'alfajor', 'turrón']):
        return 'Golosinas, Snacks y Panificados'
    
    # Limpieza del Hogar
    if any(palabra in nombre_lower for palabra in ['detergente', 'lavandina', 'desengrasante', 'limpiavidrios', 'suavizante', 'esponja', 'trapo', 'servilleta', 'papel higiénico']):
        return 'Limpieza del Hogar'
    
    # Higiene Personal
    if any(palabra in nombre_lower for palabra in ['shampoo', 'jabón', 'crema dental', 'cepillo', 'hilo dental', 'desodorante', 'toallas húmedas', 'mascarilla']):
        return 'Higiene Personal'
    
    # Almacén y Despensa
    if any(palabra in nombre_lower for palabra in ['arroz', 'fideo', 'lenteja', 'garbanzo', 'poroto', 'harina', 'azúcar', 'sal', 'aceite', 'vinagre', 'salsa de tomate', 'caldo', 'sopa instantánea', 'avena', 'granola', 'aceituna', 'stevia']):
        return 'Almacén y Despensa'
    
    # Otros Alimentos (por defecto para helados y otros)
    if any(palabra in nombre_lower for palabra in ['helado']):
        return 'Otros Alimentos'
    
    # Por defecto
    return 'Otros Alimentos'

# Aplicar categorización a los productos
productos['categoria'] = productos['nombre_producto'].apply(categorizar_producto)

# Preparar datos de ventas con client_id
np.random.seed(42)
ventas['client_id'] = np.random.choice(clientes['id_cliente'].values, size=len(ventas))

# Agregar fecha a las ventas
ventas['fecha'] = pd.date_range(start='2023-01-01', periods=len(ventas), freq='D')

print(f"  ✓ Productos cargados: {len(productos)}")
print(f"  ✓ Clientes cargados: {len(clientes)}")
print(f"  ✓ Ventas cargadas: {len(ventas)}")
print(f"  ✓ Clientes únicos en ventas: {ventas['client_id'].nunique()}")
print(f"  ✓ Categorías disponibles: {', '.join(sorted(productos['categoria'].unique()))}\n")

# ============================================================
# GRÁFICO 1: Ventas por Cliente (Barras)
# ============================================================
print("📈 Generando Gráfico 1: Ventas por Cliente (Barras)...")

ventas_por_cliente = ventas.groupby('client_id')['importe'].sum().reset_index()
ventas_por_cliente = ventas_por_cliente.sort_values('importe', ascending=False).head(20)

plt.figure(figsize=(14, 7))
bars = plt.bar(range(len(ventas_por_cliente)), ventas_por_cliente['importe'], 
               color='steelblue', edgecolor='navy', alpha=0.7)

plt.xlabel('ID de Cliente', fontsize=12, fontweight='bold')
plt.ylabel('Ventas Totales ($)', fontsize=12, fontweight='bold')
plt.title('Ventas por Cliente - Top 20 Clientes', fontsize=14, fontweight='bold', pad=20)
plt.xticks(range(len(ventas_por_cliente)), ventas_por_cliente['client_id'], rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3, linestyle='--')

for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'${int(height):,}',
             ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig('grafico1_ventas_por_cliente.png', dpi=300, bbox_inches='tight')
print("  ✓ Gráfico 1 guardado: grafico1_ventas_por_cliente.png")
plt.close()

print(f"  - Total de ventas del top cliente: ${ventas_por_cliente['importe'].max():,.2f}")
print(f"  - Promedio de ventas por cliente: ${ventas_por_cliente['importe'].mean():,.2f}\n")

# ============================================================
# GRÁFICO 2: Ventas vs Crecimiento Proyectado (Dispersión)
# ============================================================
print("📈 Generando Gráfico 2: Ventas vs Crecimiento Proyectado (Dispersión)...")

ventas['mes'] = ventas['fecha'].dt.to_period('M')
ventas_mensuales = ventas.groupby('mes')['importe'].sum().reset_index()
ventas_mensuales['mes_num'] = range(len(ventas_mensuales))

# Regresión lineal manual
X = ventas_mensuales['mes_num'].values
y = ventas_mensuales['importe'].values

n = len(X)
m = (n * np.sum(X * y) - np.sum(X) * np.sum(y)) / (n * np.sum(X**2) - np.sum(X)**2)
b = (np.sum(y) - m * np.sum(X)) / n

def predecir(x):
    return m * x + b

meses_futuros = np.array(range(len(ventas_mensuales), len(ventas_mensuales) + 6))
proyeccion_futura = np.array([predecir(mes) for mes in meses_futuros])

# Calcular crecimiento
crecimiento_proyectado = []
for i in range(len(ventas_mensuales)):
    if i > 0:
        crecimiento = ((ventas_mensuales.iloc[i]['importe'] - ventas_mensuales.iloc[i-1]['importe']) / 
                      ventas_mensuales.iloc[i-1]['importe']) * 100
    else:
        crecimiento = 0
    crecimiento_proyectado.append(crecimiento)

crecimiento_futuro = []
for i, proy in enumerate(proyeccion_futura):
    if i == 0:
        base = ventas_mensuales.iloc[-1]['importe']
    else:
        base = proyeccion_futura[i-1]
    crecimiento = ((proy - base) / base) * 100 if base > 0 else 0
    crecimiento_futuro.append(crecimiento)

ventas_totales = list(ventas_mensuales['importe']) + list(proyeccion_futura)
crecimiento_total = crecimiento_proyectado + crecimiento_futuro

plt.figure(figsize=(14, 8))

plt.scatter(ventas_mensuales['importe'], crecimiento_proyectado, 
           s=150, alpha=0.7, color='steelblue', edgecolors='navy', linewidth=2,
           label='Datos Reales', zorder=3)

plt.scatter(proyeccion_futura, crecimiento_futuro, 
           s=150, alpha=0.7, color='coral', edgecolors='darkred', linewidth=2,
           marker='s', label='Proyecciones Futuras', zorder=3)

z = np.polyfit(ventas_totales, crecimiento_total, 1)
p = np.poly1d(z)
plt.plot(sorted(ventas_totales), p(sorted(ventas_totales)), 
         "r--", alpha=0.5, linewidth=2, label='Tendencia')

plt.xlabel('Ventas Totales ($)', fontsize=12, fontweight='bold')
plt.ylabel('Crecimiento Proyectado (%)', fontsize=12, fontweight='bold')
plt.title('Ventas vs Crecimiento Proyectado a Futuro', fontsize=14, fontweight='bold', pad=20)
plt.legend(loc='best', fontsize=10, framealpha=0.9)
plt.grid(True, alpha=0.3, linestyle='--')

for i, (venta, crec) in enumerate(zip(ventas_mensuales['importe'], crecimiento_proyectado)):
    if i % 2 == 0:
        plt.annotate(f'M{i+1}', (venta, crec), fontsize=8, alpha=0.7)

plt.tight_layout()
plt.savefig('grafico2_ventas_vs_crecimiento.png', dpi=300, bbox_inches='tight')
print("  ✓ Gráfico 2 guardado: grafico2_ventas_vs_crecimiento.png")
plt.close()

print(f"  - Ventas promedio mensuales: ${ventas_mensuales['importe'].mean():,.2f}")
print(f"  - Crecimiento promedio proyectado: {np.mean(crecimiento_proyectado):.2f}%")
print(f"  - Proyección para el próximo mes: ${proyeccion_futura[0]:,.2f}\n")

# ============================================================
# GRÁFICO 3: Comparación Tradicional vs IA (Lineal)
# ============================================================
print("📈 Generando Gráfico 3: Comparación Sistema Tradicional vs IA (Lineal)...")

meses_historicos = len(ventas_mensuales)
meses_proyeccion = 12

crecimiento_tradicional = 0.03  # 3% mensual

ventas_tradicional = []
for i in range(meses_historicos + meses_proyeccion):
    if i < meses_historicos:
        ventas_tradicional.append(ventas_mensuales.iloc[i]['importe'])
    else:
        venta_anterior = ventas_tradicional[i-1]
        ventas_tradicional.append(venta_anterior * (1 + crecimiento_tradicional))

crecimiento_ia_inicial = 0.05  # 5% inicial
crecimiento_ia_acelerado = 0.08  # 8% después

ventas_ia = []
for i in range(meses_historicos + meses_proyeccion):
    if i < meses_historicos:
        ventas_ia.append(ventas_mensuales.iloc[i]['importe'])
    elif i < meses_historicos + 3:
        venta_anterior = ventas_ia[i-1]
        ventas_ia.append(venta_anterior * (1 + crecimiento_ia_inicial))
    else:
        venta_anterior = ventas_ia[i-1]
        ventas_ia.append(venta_anterior * (1 + crecimiento_ia_acelerado))

meses_totales = range(1, meses_historicos + meses_proyeccion + 1)
mes_implementacion_ia = meses_historicos + 1

plt.figure(figsize=(16, 8))

plt.plot(meses_totales, ventas_tradicional, 
        marker='o', linewidth=2.5, markersize=6,
        color='#e74c3c', label='Sistema Tradicional de Marketing',
        alpha=0.8)

plt.plot(meses_totales, ventas_ia, 
        marker='s', linewidth=2.5, markersize=6,
        color='#3498db', label='Sistema con Inteligencia Artificial',
        alpha=0.8)

plt.axvline(x=mes_implementacion_ia, color='green', linestyle='--', 
           linewidth=2, alpha=0.7, label='Implementación de IA')

diferencia = np.array(ventas_ia) - np.array(ventas_tradicional)
plt.fill_between(meses_totales, ventas_tradicional, ventas_ia, 
                where=(np.array(ventas_ia) >= np.array(ventas_tradicional)),
                alpha=0.3, color='green', label='Ventaja del Sistema con IA')

plt.xlabel('Mes', fontsize=12, fontweight='bold')
plt.ylabel('Ventas Totales ($)', fontsize=12, fontweight='bold')
plt.title('Comparación de Crecimiento: Sistema Tradicional vs Sistema con IA', 
         fontsize=14, fontweight='bold', pad=20)
plt.legend(loc='upper left', fontsize=11, framealpha=0.9, shadow=True)
plt.grid(True, alpha=0.3, linestyle='--')

diferencia_final = ventas_ia[-1] - ventas_tradicional[-1]
porcentaje_mejora = (diferencia_final / ventas_tradicional[-1]) * 100

plt.annotate(f'Mejora con IA: +${diferencia_final:,.0f}\n({porcentaje_mejora:.1f}% más)', 
            xy=(meses_totales[-1], ventas_ia[-1]),
            xytext=(meses_totales[-1] - 3, ventas_ia[-1] + max(ventas_ia) * 0.1),
            fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2', color='black'))

plt.tight_layout()
plt.savefig('grafico3_comparacion_tradicional_vs_ia.png', dpi=300, bbox_inches='tight')
print("  ✓ Gráfico 3 guardado: grafico3_comparacion_tradicional_vs_ia.png")
plt.close()

print("\n" + "=" * 60)
print("COMPARACIÓN DE SISTEMAS")
print("=" * 60)
print(f"\nSistema Tradicional:")
print(f"  - Ventas finales: ${ventas_tradicional[-1]:,.2f}")
print(f"  - Crecimiento acumulado: {((ventas_tradicional[-1] / ventas_tradicional[0]) - 1) * 100:.2f}%")

print(f"\nSistema con IA:")
print(f"  - Ventas finales: ${ventas_ia[-1]:,.2f}")
print(f"  - Crecimiento acumulado: {((ventas_ia[-1] / ventas_ia[0]) - 1) * 100:.2f}%")

print(f"\nVentaja del Sistema con IA:")
print(f"  - Diferencia absoluta: ${diferencia_final:,.2f}")
print(f"  - Mejora porcentual: {porcentaje_mejora:.2f}%")

# ============================================================
# GRÁFICO 4: HeatMap de Ventas por Mes y Categoría de Producto
# ============================================================
print("📈 Generando Gráfico 4: HeatMap de Ventas por Mes y Categoría de Producto...")

# Preparar datos para el HeatMap: unir ventas con productos para obtener categorías
ventas_con_categorias = ventas.merge(
    productos[['id_producto', 'categoria']],
    on='id_producto',
    how='left'
)

# Preparar datos para el HeatMap
ventas_con_categorias['mes'] = ventas_con_categorias['fecha'].dt.to_period('M')
ventas_con_categorias['mes_str'] = ventas_con_categorias['mes'].astype(str)

# Crear matriz de ventas: Meses (filas) x Categorías (columnas)
heatmap_data = ventas_con_categorias.pivot_table(
    values='importe',
    index='mes_str',
    columns='categoria',
    aggfunc='sum',
    fill_value=0
)

# Ordenar por mes cronológicamente
heatmap_data = heatmap_data.sort_index()

# Ordenar categorías por ventas totales (de mayor a menor) para mejor visualización
categorias_ordenadas = heatmap_data.sum().sort_values(ascending=False).index
heatmap_data = heatmap_data[categorias_ordenadas]

# Crear el HeatMap con mejor tamaño para las etiquetas
plt.figure(figsize=(18, 10))

# Usar seaborn para crear el heatmap con mejor visualización
ax = sns.heatmap(
    heatmap_data,
    annot=True,
    fmt='.0f',
    cmap='YlOrRd',  # Colores cálidos: amarillo-naranja-rojo
    cbar_kws={'label': 'Ventas ($)', 'shrink': 0.8, 'pad': 0.02},
    linewidths=0.8,
    linecolor='white',
    square=False,
    annot_kws={'size': 9, 'weight': 'bold'},
    xticklabels=True,
    yticklabels=True
)

# Personalizar etiquetas de categorías (eje X) - rotar y ajustar tamaño
categorias_labels = [cat.replace(' y ', '\ny ') for cat in heatmap_data.columns]
ax.set_xticklabels(categorias_labels, rotation=45, ha='right', fontsize=11, fontweight='bold')
ax.set_yticklabels(heatmap_data.index, rotation=0, fontsize=11, fontweight='bold')

# Personalizar gráfico
plt.xlabel('Categorías de Productos', fontsize=14, fontweight='bold', labelpad=15)
plt.ylabel('Mes', fontsize=14, fontweight='bold', labelpad=10)
plt.title('HeatMap de Ventas: Ventas por Mes y Categoría de Producto - Tienda Aurelion', 
         fontsize=16, fontweight='bold', pad=25)

plt.tight_layout()
plt.savefig('grafico4_heatmap_ventas_mes_categoria.png', dpi=300, bbox_inches='tight')
print("  ✓ Gráfico 4 guardado: grafico4_heatmap_ventas_mes_categoria.png")
plt.close()

# Estadísticas del HeatMap
print("\n=== ANÁLISIS DEL HEATMAP POR CATEGORÍAS ===")
print(f"  - Total de meses analizados: {len(heatmap_data)}")
print(f"  - Total de categorías: {len(heatmap_data.columns)}")
print(f"  - Categorías disponibles: {', '.join(heatmap_data.columns.tolist())}")
print(f"\n  - Categoría con mayor venta total: {heatmap_data.sum().idxmax()}")
print(f"  - Ventas totales de la categoría top: ${heatmap_data.sum().max():,.2f}")
print(f"  - Mes con mayor venta total: {heatmap_data.sum(axis=1).idxmax()}")
print(f"  - Ventas totales del mes top: ${heatmap_data.sum(axis=1).max():,.2f}")
print(f"  - Promedio de ventas por celda: ${heatmap_data.values.mean():,.2f}")
print(f"\n  - Desglose por categoría:")
for categoria in categorias_ordenadas:
    total_categoria = heatmap_data[categoria].sum()
    porcentaje = (total_categoria / heatmap_data.sum().sum()) * 100
    print(f"    • {categoria}: ${total_categoria:,.2f} ({porcentaje:.1f}% del total)\n")

print("\n" + "=" * 60)
print("✅ TODOS LOS GRÁFICOS GENERADOS EXITOSAMENTE")
print("=" * 60)
print("\nArchivos generados:")
print("  📊 grafico1_ventas_por_cliente.png")
print("  📊 grafico2_ventas_vs_crecimiento.png")
print("  📊 grafico3_comparacion_tradicional_vs_ia.png")
print("  📊 grafico4_heatmap_ventas_mes_categoria.png")
print("\n")

