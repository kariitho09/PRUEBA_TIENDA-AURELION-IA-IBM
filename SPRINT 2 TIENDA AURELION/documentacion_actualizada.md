# Documentación del Proyecto Aurelion

## Tema
Este proyecto simula la gestión de la Tienda Aurelion utilizando datos sintéticos en Python, enfocándose en análisis de datos, visualización y modelado para un contexto de negocio minorista.

El objetivo es disponer de un escenario práctico y consistente para aplicar técnicas de análisis de datos, visualización y modelado en un contexto de negocio real, como una tienda minorista.

## Problema
La falta de escenarios prácticos y consistentes para aplicar técnicas de análisis de datos en entornos educativos, especialmente en simulaciones de tiendas con productos, clientes y ventas.

Específicamente, la falta de un escenario práctico y consistente para aplicar técnicas de análisis de datos, visualización y modelado en un contexto de negocio real, como una tienda minorista.

## Solución
Desarrollo de datasets sintéticos limpios (productos_demo2.csv, clientes_demo2.csv, detalle_ventas_demo2.csv) y un programa en Python (.py) con menú interactivo para explorar documentación y análisis. Incluye estadísticas descriptivas, distribuciones, correlaciones, detección de outliers y gráficos.

Desarrollar un conjunto de datos sintéticos que representen las operaciones de la Tienda Aurelion, incluyendo productos, clientes y ventas, con el objetivo de disponer de un escenario consistente para practicar análisis, visualización y modelado.

## Estructura de Datos
- **Productos (productos_demo2.csv)**: ~100 filas
  - `id_producto`: Entero (Ratio)
  - `nombre_producto`: Texto (Nominal)
  - `categoria`: Texto (Nominal) - 11 categorías
  - `precio_unitario`: Decimal (Ratio)

- **Clientes (clientes_demo2.csv)**: ~100 filas
  - `id_cliente`: Entero (Ratio)
  - `nombre_cliente`: Texto (Nominal)
  - `email`: Texto (Nominal)
  - `ciudad`: Texto (Nominal)
  - `fecha_alta`: Fecha (Ordinal)

- **Ventas (detalle_ventas_demo2.csv)**: ~343 filas
  - `id_venta`: Entero (Ratio)
  - `id_producto`: Entero (Ratio)
  - `nombre_producto`: Texto (Nominal)
  - `cantidad`: Entero (Ratio)
  - `precio_unitario`: Decimal (Ratio)
  - `importe`: Decimal (Ratio)

## Escalas de Medición
- **Nominal**: Categoría, género, ubicación, nombre, email, ciudad
- **Ordinal**: Fecha (fecha_alta)
- **Ratio**: Precio, stock, edad, cantidad, importe, id_producto, id_cliente, id_venta

Las escalas de medición permiten determinar qué tipo de análisis estadístico es apropiado para cada variable.

## Análisis Realizado

### Estadísticas Descriptivas
- Media, mediana, desviación estándar para variables numéricas
- Análisis de distribución de precios, cantidades e importes
- Identificación de valores atípicos (outliers)

### Distribuciones
- **Precios**: Distribución que permite identificar productos premium y económicos
- **Cantidades**: Distribución de unidades vendidas por transacción
- **Importes**: Distribución de valores de venta totales

### Outliers
- Detectados en precios altos y ventas extremas usando método IQR (Interquartile Range)
- Los outliers indican productos premium o transacciones excepcionales
- Útiles para identificar oportunidades de negocio o errores en los datos

### Gráficos Generados
1. **Histograma de precios**: Distribución de precios de productos
2. **Diagrama de dispersión precio-cantidad**: Relación entre precio y cantidad vendida
3. **Gráfico de barras**: Ventas por cliente (Top 20)
4. **Gráfico de dispersión**: Ventas vs crecimiento proyectado
5. **Gráfico lineal comparativo**: Sistema tradicional vs sistema con IA
6. **HeatMap**: Ventas por mes y categoría de producto

### Interpretación
- Outliers indican productos premium que pueden requerir estrategias de marketing diferenciadas
- Las correlaciones guían estrategias de precios y gestión de inventario
- Los patrones temporales ayudan en la planificación de compras y promociones

## Patrones, Tendencias y Correlaciones Identificadas

### Correlaciones

#### 1. Correlación Precio vs Cantidad Vendida
- **Valor**: -0.074 (correlación negativa débil)
- **Interpretación**: Existe una ligera tendencia negativa, lo que sugiere que a mayor precio, menor cantidad vendida. Esto es consistente con la teoría económica básica de demanda.
- **Implicación**: Los productos más caros tienden a venderse en menores cantidades, lo que puede indicar que son productos premium o de compra ocasional.

#### 2. Correlación Precio vs Importe Total
- **Valor**: 0.679 (correlación positiva moderada-fuerte)
- **Interpretación**: Existe una correlación positiva significativa entre el precio unitario y el importe total de la venta.
- **Implicación**: Los productos con mayor precio contribuyen significativamente al importe total, lo que sugiere que una estrategia de precios premium puede ser efectiva para aumentar los ingresos.

### Patrones Temporales

#### 1. Variación Mensual de Ventas
- **Patrón identificado**: Las ventas muestran variación a lo largo de los meses del año
- **Mes con mayor venta**: Abril (Mes 4) - período de mayor actividad comercial
- **Mes con menor venta**: Diciembre (Mes 12) - posiblemente debido a cierre de año o estacionalidad
- **Tendencia**: Existe estacionalidad en las ventas que debe considerarse para la planificación de inventario y promociones

#### 2. Patrones por Categoría
Las categorías muestran diferentes patrones de venta:
- **Bebidas sin Alcohol**: Categoría líder en ventas, con demanda constante
- **Almacén y Despensa**: Segunda categoría más importante, productos de consumo regular
- **Golosinas, Snacks y Panificados**: Alta rotación, productos de compra impulsiva

### Tendencias Identificadas

#### 1. Concentración de Ventas por Categoría
- **Top 3 categorías** representan aproximadamente el 47.4% del total de ventas:
  1. Bebidas sin Alcohol (21.0%)
  2. Almacén y Despensa (14.0%)
  3. Golosinas, Snacks y Panificados (12.4%)
- **Tendencia**: Alta concentración en categorías de consumo diario y frecuente

#### 2. Distribución de Clientes
- **Patrón**: Los clientes muestran diferentes niveles de gasto
- **Top 20 clientes**: Representan una porción significativa de las ventas totales
- **Tendencia**: Existe un grupo de clientes de alto valor que requiere estrategias de retención específicas

#### 3. Crecimiento Proyectado
- **Sistema Tradicional**: Crecimiento lineal moderado (3% mensual)
- **Sistema con IA**: Crecimiento exponencial mejorado (5-8% mensual)
- **Tendencia**: La implementación de IA muestra un potencial de mejora del 62.31% en ventas proyectadas

### Patrones de Comportamiento

#### 1. Relación Precio-Cantidad
- Los productos de menor precio tienden a venderse en mayores cantidades
- Los productos premium tienen menor rotación pero mayor margen por unidad
- **Estrategia sugerida**: Balancear el mix de productos entre alta rotación y alto margen

#### 2. Estacionalidad
- Diferentes meses muestran diferentes niveles de actividad
- Algunas categorías pueden tener picos estacionales específicos
- **Estrategia sugerida**: Planificar inventario y promociones según patrones estacionales identificados

#### 3. Segmentación por Categoría
- Las 11 categorías muestran diferentes perfiles de venta:
  - **Alto volumen**: Bebidas sin Alcohol, Almacén y Despensa
  - **Volumen medio**: Lácteos, Bebidas con Alcohol, Higiene Personal
  - **Volumen bajo pero estratégico**: Panadería, Untables, Otros Alimentos
- **Estrategia sugerida**: Estrategias diferenciadas por categoría según su perfil de venta

### Correlaciones Adicionales Identificadas

#### 1. Relación entre Categoría y Precio Promedio
- Diferentes categorías tienen diferentes rangos de precios
- Las categorías premium (Bebidas con Alcohol) tienen precios más altos
- Las categorías básicas (Almacén y Despensa) tienen precios más accesibles

#### 2. Relación entre Mes y Categoría
- El HeatMap revela que ciertas categorías tienen picos en meses específicos
- Algunas categorías mantienen ventas constantes a lo largo del año
- **Insight**: Permite optimizar el inventario por categoría según el mes

### Proyecto
Tienda Aurelion
● Documentación: notebook Markdown
● Desarrollo técnico: programa Python
● Visualización de datos: dashboard en Power BI
● Presentación oral: problema, solución y hallazgos

### Diseño conceptual ML(machine learning):
En relación a la base de datos.
1.Deﬁne el objetivo (predecir o clasiﬁcar)
2.Elige y justiﬁca el algoritmo
3.Indica entradas (X) y salida (y)
4.Especiﬁca las métricas de evaluación


## Programa (.py)
Sistema integrado con menú interactivo (`aurelion_menu_unificado.py`) que incluye:
- Visualización de datos
- Análisis estadístico
- Generación de gráficos
- Documentación del proyecto
- Generación de gráficos completos
- Generación de presentación HTML

## Mejoras con Copilot
Sugerencias implementadas y futuras:
- ✅ Integración de análisis de categorías automático
- ✅ Visualizaciones interactivas (HeatMap, gráficos comparativos)
- ✅ Sistema de presentación HTML
- 🔄 Integrar machine learning para predicción de ventas
- 🔄 Dashboard interactivo con gráficos dinámicos
- 🔄 Análisis de segmentación de clientes avanzado
- 🔄 Sistema de recomendaciones basado en compras previas
- 🔄 Análisis de tendencias temporales avanzadas

## Archivos del Proyecto
- `productos_demo2.csv`: Catálogo de productos
- `clientes_demo2.csv`: Base de datos de clientes
- `detalle_ventas_demo2.csv`: Registro de transacciones
- `aurelion_menu_unificado.py`: Menú principal interactivo
- `ejecutar_graficos.py`: Generador de gráficos completos
- `generar_presentacion.py`: Generador de presentación HTML
- `presentacion_aurelion.html`: Presentación interactiva del proyecto
