# Datos hipotéticos para Detalle_Ventas (basado en la descripción del proyecto)
data = {
    'id_venta': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
    'cantidad': [2, 1, 3, 2, 1, 4, 2, 3, 1, 2],
    'precio_unitario': [100, 150, 200, 100, 250, 150, 300, 200, 100, 150],
    'importe': [200, 150, 600, 200, 250, 600, 600, 600, 100, 300]
}
df = pd.DataFrame(data)
print("DataFrame de ejemplo:")
print(df)