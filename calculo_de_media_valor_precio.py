# Mediana para columnas numéricas
mediana_precio = df['precio_unitario'].median()
mediana_cantidad = df['cantidad'].median()
mediana_importe = df['importe'].median()

print("Mediana (Valor Central):")
print(f"- Precio Unitario: {mediana_precio}")
print(f"- Cantidad: {mediana_cantidad}")
print(f"- Importe: {mediana_importe}")