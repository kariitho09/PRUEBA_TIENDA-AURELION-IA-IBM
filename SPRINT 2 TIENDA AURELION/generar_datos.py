import pandas as pd
import numpy as np
from faker import Faker
import random

# Inicializar Faker para generar datos sintéticos
fake = Faker('es_ES')

# --- Cargar datos existentes ---
try:
    clientes_df = pd.read_csv('clientes_demo2.csv')
    productos_df = pd.read_csv('productos_demo2.csv')
    ventas_df = pd.read_csv('detalle_ventas_demo2.csv')
except FileNotFoundError:
    print("Asegúrate de que los archivos 'clientes_demo2.csv', 'productos_demo2.csv' y 'detalle_ventas_demo2.csv' estén en el mismo directorio.")
    exit()

# --- Generar Nuevos Clientes ---
print("Generando nuevos clientes...")
nuevos_clientes = []
id_cliente_actual = clientes_df['id_cliente'].max() + 1
for i in range(50):
    nombre = fake.first_name()
    apellido = fake.last_name()
    nuevos_clientes.append({
        'id_cliente': id_cliente_actual + i,
        'nombre_cliente': f"{nombre} {apellido}",
        'email': f"{nombre.lower()}.{apellido.lower()}{i}@mail.com",
        'ciudad': fake.city(),
        'fecha_alta': fake.date_between(start_date='-2y', end_date='today')
    })

nuevos_clientes_df = pd.DataFrame(nuevos_clientes)
clientes_actualizado_df = pd.concat([clientes_df, nuevos_clientes_df], ignore_index=True)

# --- Generar Nuevos Productos ---
print("Generando nuevos productos...")
nuevos_productos = []
id_producto_actual = productos_df['id_producto'].max() + 1
categorias = ['Alimentos', 'Limpieza', 'Hogar', 'Bebidas']
for i in range(20):
    nuevos_productos.append({
        'id_producto': id_producto_actual + i,
        'nombre_producto': f"Producto Nuevo {i+1}",
        'categoria': random.choice(categorias),
        'precio_unitario': round(random.uniform(500, 10000), 2)
    })

nuevos_productos_df = pd.DataFrame(nuevos_productos)
productos_actualizado_df = pd.concat([productos_df, nuevos_productos_df], ignore_index=True)


# --- Generar Nuevos Detalles de Venta ---
print("Generando nuevos detalles de venta...")
nuevas_ventas = []
id_venta_actual = ventas_df['id_venta'].max() + 1
for i in range(200):
    producto_elegido = productos_actualizado_df.sample(1).iloc[0]
    cantidad = random.randint(1, 5)
    
    nuevas_ventas.append({
        'id_venta': id_venta_actual + i,
        'id_producto': producto_elegido['id_producto'],
        'nombre_producto': producto_elegido['nombre_producto'],
        'cantidad': cantidad,
        'precio_unitario': producto_elegido['precio_unitario'],
        'importe': round(cantidad * producto_elegido['precio_unitario'], 2)
    })

nuevas_ventas_df = pd.DataFrame(nuevas_ventas)
ventas_actualizado_df = pd.concat([ventas_df, nuevas_ventas_df], ignore_index=True)


# --- Guardar los nuevos dataframes en la carpeta DEMO 3 ---
output_dir = 'DEMO 3'
print(f"Guardando archivos en '{output_dir}'...")

clientes_actualizado_df.to_csv(f'{output_dir}/clientes_demo3.csv', index=False)
productos_actualizado_df.to_csv(f'{output_dir}/productos_demo3.csv', index=False)
ventas_actualizado_df.to_csv(f'{output_dir}/detalle_ventas_demo3.csv', index=False)

print("\n¡Proceso completado!")
print(f"Se generaron {len(nuevos_clientes_df)} clientes nuevos.")
print(f"Se generaron {len(nuevos_productos_df)} productos nuevos.")
print(f"Se generaron {len(nuevas_ventas_df)} registros de ventas nuevos.")
print(f"Archivos guardados en la carpeta '{output_dir}'.")
