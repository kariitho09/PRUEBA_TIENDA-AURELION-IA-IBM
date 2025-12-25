# Media para columnas numéricas
media_precio = df['precio_unitario'].mean()
media_cantidad = df['cantidad'].mean()
media_importe = df['importe'].mean()

print("Media (Promedio):")
print(f"- Precio Unitario: {media_precio}")
print(f"- Cantidad: {media_cantidad}")
print(f"- Importe: {media_importe}")