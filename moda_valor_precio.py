# Moda para columnas numéricas
moda_precio = df['precio_unitario'].mode()
moda_cantidad = df['cantidad'].mode()
moda_importe = df['importe'].mode()

print("Moda (Valor Más Frecuente):")
print(f"- Precio Unitario: {moda_precio.tolist()}")
print(f"- Cantidad: {moda_cantidad.tolist()}")
print(f"- Importe: {moda_importe.tolist()}")