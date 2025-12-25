# Reporte del Modelo de Machine Learning - Tienda Aurelion

Este documento detalla las especificaciones del sistema de Machine Learning implementado en `aurelion_ml_system.py`.

## 1. Definición del Objetivo

El sistema tiene un **doble objetivo**, abordando tanto problemas de predicción (regresión) como de clasificación:

*   **Predicción (Regresión):** Estimar el **monto total de la venta** (`total_amount`) basándose en las características del producto y del cliente. Esto permite prever ingresos y entender qué factores impulsan el valor de las ventas.
*   **Clasificación:** Predecir la **categoría del producto** (`category`) basándose en sus atributos y patrones de venta. Esto puede ayudar a segmentar inventario o recomendar categorías.

## 2. Elección y Justificación del Algoritmo

Se han seleccionado dos algoritmos estándar de la librería `scikit-learn`:

### Para Regresión: **Linear Regression (Regresión Lineal)**
*   **Justificación:** Es un algoritmo fundamental y eficiente para establecer una línea base. Permite interpretar fácilmente la relación entre las variables de entrada (como precio o stock) y la variable objetivo (monto de venta). Es ideal para identificar tendencias lineales simples en los datos comerciales.

### Para Clasificación: **K-Nearest Neighbors (KNN)**
*   **Justificación:** El algoritmo de "K-Vecinos Más Cercanos" (con `n_neighbors=5`) es un método no paramétrico simple pero efectivo. Clasifica un dato basándose en la similitud con los datos históricos más cercanos. Es útil cuando las fronteras de decisión no son necesariamente lineales y se dispone de un conjunto de datos etiquetado.

## 3. Entradas (X) y Salidas (y)

### Variables de Entrada (Features - X)
El modelo utiliza las siguientes características para realizar sus predicciones:

1.  **price**: Precio del producto.
2.  **stock**: Nivel de stock disponible.
3.  **rating**: Calificación promedio del producto.
4.  **reviews**: Cantidad de reseñas.
5.  **customer_age**: Edad del cliente.
6.  **discount**: Descuento aplicado.
7.  **season_encoded**: Estación del año (codificada numéricamente).
8.  **day_encoded**: Día de la semana (codificado numéricamente).
9.  **category_encoded**: Categoría del producto (codificada numéricamente). *(Nota: Utilizada principalmente para el modelo de regresión)*.

### Variables de Salida (Target - y)

*   **Modelo de Regresión ($y_{reg}$):** `total_amount` (Monto total de la transacción).
*   **Modelo de Clasificación ($y_{class}$):** `category` (Categoría a la que pertenece el producto, ej: Electrónicos, Ropa, Hogar).

## 4. Métricas de Evaluación

Para medir el desempeño de los modelos se utilizan las siguientes métricas:

### Métricas de Regresión
*   **RMSE (Root Mean Squared Error):** La raíz del error cuadrático medio. Indica cuánto se desvían las predicciones del valor real en las mismas unidades que la variable objetivo (dólares/pesos).
*   **MAE (Mean Absolute Error):** El promedio de los errores absolutos. Es una medida robusta de la magnitud del error.
*   **R² (Coeficiente de Determinación):** Indica qué proporción de la varianza en la variable objetivo es explicada por el modelo (0 a 1).

### Métricas de Clasificación
*   **Accuracy (Exactitud):** El porcentaje total de predicciones correctas sobre el total de casos.
*   **Confusion Matrix (Matriz de Confusión):** Una tabla que permite visualizar el desempeño del algoritmo, mostrando los verdaderos positivos, falsos positivos, verdaderos negativos y falsos negativos por cada categoría.
