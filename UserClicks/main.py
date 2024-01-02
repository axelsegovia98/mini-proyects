import pandas as pd

nombres_columnas = ['ID', 'Inicio', 'Fin', 'Correo', 'Detalles']
final_columnas = ['ID', 'Inicio', 'Fin', 'Correo','Marca']

# Cargar el archivo CSV en un DataFrame
ruta_archivo = 'InteraccionesStands-_1_.csv'
datos = pd.read_csv(ruta_archivo,skiprows=1, header=None)
datos.columns = nombres_columnas

# Mostrar los primeros registros para verificar la carga de datos
print(datos.head())

# Función para extraer la información después de "brand:" utilizando expresiones regulares
def extraer_marca(detalle):
    import re
    matches = re.findall(r'brand:\s*(\w+)', detalle)
    return matches

# Aplicar la función a la columna 'Detalles' para extraer la información de marca
datos['Marca'] = datos['Detalles'].apply(extraer_marca)

# datos_nuevos = datos[final_columnas].copy()

# conteo_marcas = {}
# for lista_marcas in datos['Marca']:
#     for marca in lista_marcas:
#         if marca in conteo_marcas:
#             conteo_marcas[marca] += 1
#         else:
#             conteo_marcas[marca] = 1

# # Mostrar el conteo de las marcas
# for marca, cantidad in conteo_marcas.items():
#     print(f"{marca}: {cantidad}")


# Duplicar filas por cada marca en la lista
datos_expandidos = datos.explode('Marca')
total_por_marca = datos_expandidos.groupby(['Correo', 'Marca']).size().reset_index(name='Total')

print(total_por_marca)

datos_nuevos = datos_expandidos[final_columnas].copy()


# Mostrar el DataFrame con la columna 'Marca' añadida
ruta_salida_1 = 'datos_modificados.csv'  # Nombre y ruta del archivo de salida
datos_nuevos.to_csv(ruta_salida_1, index=False)  # Guardar sin incluir el índice del DataFrame en el archivo CSV

ruta_salida_2 = 'total_usuario_stand.csv'  # Nombre y ruta del archivo de salida
total_por_marca.to_csv(ruta_salida_2, index=False)  # Guardar sin incluir el índice del DataFrame en el archivo CSV