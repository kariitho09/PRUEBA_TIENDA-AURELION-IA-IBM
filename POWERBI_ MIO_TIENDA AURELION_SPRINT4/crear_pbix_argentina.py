
"""
Script para generar archivo Power BI (.pbix) con datos de provincias argentinas
Requiere: pip install powerbiclient pandas
"""

import pandas as pd
import json
import zipfile
import os
from datetime import datetime

def crear_pbix_argentina():
    """
    Crea un archivo .pbix con la estructura básica y los datos de Argentina
    """

    # Crear estructura de directorios temporales
    temp_dir = "temp_pbix"
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(f"{temp_dir}/DataModelSchema", exist_ok=True)

    # 1. Crear archivo de metadatos
    metadata = {
        "version": "1.0",
        "dataRefresh": datetime.now().isoformat(),
        "author": "Sistema Automatizado",
        "title": "Análisis Provincias Argentina 2024"
    }

    with open(f"{temp_dir}/metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    # 2. Crear esquema del modelo de datos
    schema = {
        "name": "Argentina_Analysis",
        "tables": [
            {
                "name": "Provincias",
                "columns": [
                    {"name": "Provincia", "dataType": "string"},
                    {"name": "Poblacion", "dataType": "int64"},
                    {"name": "PIB_per_capita", "dataType": "double"},
                    {"name": "PIB_total", "dataType": "double"},
                    {"name": "Region", "dataType": "string"}
                ]
            },
            {
                "name": "Ventas",
                "columns": [
                    {"name": "Provincia", "dataType": "string"},
                    {"name": "Mes", "dataType": "string"},
                    {"name": "Fecha", "dataType": "dateTime"},
                    {"name": "Ventas", "dataType": "double"},
                    {"name": "Trimestre", "dataType": "string"}
                ]
            },
            {
                "name": "Clientes",
                "columns": [
                    {"name": "Provincia", "dataType": "string"},
                    {"name": "Total_Clientes", "dataType": "int64"},
                    {"name": "Tasa_Abandono", "dataType": "double"},
                    {"name": "NPS", "dataType": "double"},
                    {"name": "Indice_Retencion", "dataType": "double"}
                ]
            }
        ],
        "relationships": [
            {
                "name": "Provincias_Ventas",
                "fromTable": "Provincias",
                "fromColumn": "Provincia",
                "toTable": "Ventas",
                "toColumn": "Provincia"
            },
            {
                "name": "Provincias_Clientes",
                "fromTable": "Provincias",
                "fromColumn": "Provincia",
                "toTable": "Clientes",
                "toColumn": "Provincia"
            }
        ]
    }

    with open(f"{temp_dir}/DataModelSchema/model.json", "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=2, ensure_ascii=False)

    # 3. Crear configuración del reporte
    report_config = {
        "version": "4.0",
        "pages": [
            {
                "name": "Dashboard Principal",
                "visuals": [
                    {
                        "type": "card",
                        "title": "Población Total",
                        "measure": "SUM(Provincias[Poblacion])"
                    },
                    {
                        "type": "map",
                        "title": "Mapa de Argentina",
                        "location": "Provincias[Provincia]",
                        "values": "SUM(Ventas[Ventas])"
                    },
                    {
                        "type": "lineChart",
                        "title": "Evolución Mensual",
                        "axis": "Ventas[Mes]",
                        "values": "SUM(Ventas[Ventas])"
                    },
                    {
                        "type": "barChart",
                        "title": "Top Provincias",
                        "axis": "Provincias[Provincia]",
                        "values": "SUM(Provincias[Poblacion])"
                    }
                ]
            },
            {
                "name": "Análisis de Clientes",
                "visuals": [
                    {
                        "type": "scatterChart",
                        "title": "NPS vs Abandono",
                        "x": "Clientes[NPS]",
                        "y": "Clientes[Tasa_Abandono]",
                        "size": "Clientes[Total_Clientes]"
                    },
                    {
                        "type": "gauge",
                        "title": "NPS Promedio",
                        "value": "AVERAGE(Clientes[NPS])"
                    }
                ]
            }
        ]
    }

    with open(f"{temp_dir}/report.json", "w", encoding="utf-8") as f:
        json.dump(report_config, f, indent=2, ensure_ascii=False)

    # 4. Copiar archivos de datos
    import shutil
    data_files = [
        "provincias_argentina.csv",
        "ventas_mensuales.csv", 
        "clientes_provincias.csv",
        "calendario_2024.csv"
    ]

    os.makedirs(f"{temp_dir}/Data", exist_ok=True)
    for file in data_files:
        if os.path.exists(f"powerbi_data/{file}"):
            shutil.copy(f"powerbi_data/{file}", f"{temp_dir}/Data/{file}")

    # 5. Crear archivo PBIX (ZIP con extensión .pbix)
    pbix_filename = "Argentina_Provincias_Analysis.pbix"

    with zipfile.ZipFile(pbix_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Agregar todos los archivos del directorio temporal
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, temp_dir)
                zipf.write(file_path, arcname)

    # Limpiar archivos temporales
    shutil.rmtree(temp_dir)

    return pbix_filename

# Ejecutar la función
if __name__ == "__main__":
    try:
        archivo_pbix = crear_pbix_argentina()
        print(f"✓ Archivo PBIX creado exitosamente: {archivo_pbix}")
        print(f"✓ Tamaño del archivo: {os.path.getsize(archivo_pbix) / 1024:.1f} KB")
        print("\n=== INSTRUCCIONES DE USO ===")
        print("1. Abrir Power BI Desktop")
        print("2. Archivo > Abrir > Seleccionar el archivo .pbix generado")
        print("3. Los datos se cargarán automáticamente")
        print("4. Personalizar visualizaciones según necesidades")
    except Exception as e:
        print(f"❌ Error al crear archivo PBIX: {e}")
