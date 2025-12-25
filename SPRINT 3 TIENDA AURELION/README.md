# 🏪 Minimarket Aurelion – Proyecto Integral

Este proyecto combina un potente pipeline de análisis de datos y machine learning para ventas minoristas con una interfaz de usuario moderna basada en React.

- **Autor:** Diego Armando Vásquez Chávez y Carolina Veloso Salazar
- **Curso:** Fundamentos de la IA – IBM & Guayerd
- **Versión:** 3.0 (Integrada)
- **Fecha:** 2025-12-01
- **Grupo:** 3

---

## 📘 Backend y Análisis de Datos

El núcleo del sistema identifica productos estrella, estacionalidad y segmentación ABC de clientes y artículos. El pipeline integra, limpia y analiza datos provenientes de archivos (Excel/CSV/JSON), y exporta métricas, visualizaciones y resúmenes ejecutivos.

### Puntos Destacados del Backend
- **Simulación Avanzada:** Distribución de medios de pago preservada por muestreo estratificado.
- **Limpieza Robusta:** Validaciones de integridad (claves, FKs, fechas, precios) y reglas de negocio.
- **EDA Completo:** KPIs (ticket promedio, top 5, correlaciones) y clasificación ABC.
- **Logging:** Registro estructurado (JSONL) y métricas de ejecución.

### 🏗️ Arquitectura del Backend

Componentes principales:

- **Notebooks:**
   - `4. simulador_datos_comerciales.ipynb`: Genera datasets simulados.
   - `7. Limpieza_datos.ipynb`: Integra y limpia datos; exporta `*_clean.xlsx`.
   - `8. EDA_Aurelion.ipynb`: EDA y visualizaciones; genera CSV y PNG.
- **Scripts:**
   - `2. programa.py`: Orquestador del pipeline (limpieza, KPIs, export, logs).
   - `regenerar_pipeline.py`: Verificación rápida y ejecución no interactiva.
- **Paquete `aurelion/`:**
   - `pipeline_utils.py`: Configuración, lectura, validaciones.
   - `logging_utils.py`: Logging estructurado.
   - `visualization_utils.py`: Generación de gráficos.
   - `eda_analyzer.py`: Análisis de KPIs y reportes.

### ▶️ Ejecución del Backend

**Requisitos:** Python 3.10+ y paquetes: `pandas`, `numpy`, `matplotlib`, `seaborn`, `openpyxl`.

Flujo recomendado en terminal:

```powershell
# 1) (Opcional) Generar datos simulados
python "4. simulador_datos_comerciales.py"

# 2) Ejecutar el pipeline (menú interactivo)
python "2. programa.py"

# 3) (Alternativa no interactiva)
python regenerar_pipeline.py

# 4) EDA manual
# Abrir y ejecutar: 8. EDA_Aurelion.ipynb
```

---

## 💻 Frontend (Interfaz de Usuario)

La interfaz de usuario está construida con tecnologías web modernas para visualizar los datos y gestionar la tienda.

### Tecnologías

Este proyecto utiliza las siguientes tecnologías:

- **Vite**: Herramienta de construcción rápida.
- **TypeScript**: JavaScript con tipado estático.
- **React**: Biblioteca para interfaces de usuario.
- **shadcn-ui**: Componentes de UI reutilizables.
- **Tailwind CSS**: Framework de utilidades CSS.

### Requisitos Previos

Asegúrate de tener **Node.js** y **npm** instalados en tu sistema.
Recomendamos usar [nvm](https://github.com/nvm-sh/nvm#installing-and-updating) para gestionar las versiones de Node.js.

### Instalación y Desarrollo

1.  **Instalar Dependencias:**

    ```sh
    npm install
    ```

2.  **Servidor de Desarrollo:**
    Inicia el servidor con recarga en caliente (hot reload):

    ```sh
    npm run dev
    ```

3.  **Construir para Producción:**

    ```sh
    npm run build
    ```

4.  **Previsualizar Build:**

    ```sh
    npm run preview
    ```

### Estructura del Frontend

```
src/
├── components/     # Componentes de UI
├── pages/         # Componentes de Página
├── hooks/         # Hooks Personalizados
├── lib/           # Librería de Utilidades
└── main.tsx       # Punto de Entrada de la Aplicación
```

---

## 📊 Resultados Generales

El sistema genera diversos reportes y archivos en las carpetas `export/`, `visualizaciones_EDA/` y `logs/`.

- **Exportaciones:** Distribución de ventas, Top 5 productos, Correlaciones, Clasificación ABC, Outliers.
- **Visualizaciones:** Gráficos de barras, mapas de calor, diagramas de Pareto.
- **Logs:** Registros de ejecución y errores en formato JSONL.

## 🚀 Próximos Pasos

- Procesamiento por chunks para grandes volúmenes de datos.
- Dashboards interactivos integrados en el frontend.
- Validaciones extendidas y reglas de negocio dinámicas.
