import pandas as pd

# Ruta al archivo Excel
url = "Precios_pandas.xlsx"

# Leer el archivo Excel en un DataFrame
df = pd.read_excel(url)

# Imprimir el DataFrame original
print("DataFrame original:")
print(df)

# Obtener el índice de la última celda escrita en la columna 'dolar'
ultimo_indice = df['dolar'].last_valid_index()

# Obtener el valor del dólar actual a partir del último índice
dolar_actual = df['dolar'].iloc[ultimo_indice]

# Obtener el valor del dólar anterior a partir del penúltimo índice
dolar_anterior = df['dolar'].iloc[ultimo_indice - 1]

# Calcular el porcentaje de cambio en el valor del dólar
porcentaje_cambio_dolar = ((dolar_actual - dolar_anterior) / dolar_anterior) * 100

print("Dólar anterior:", dolar_anterior)
print("Dólar actual:", dolar_actual)
print("Porcentaje de cambio en el valor del dólar:", porcentaje_cambio_dolar)

# Actualizar los precios de acuerdo al porcentaje de cambio en el valor del dólar
df['Precios'] = df['Precios'] * (1 + porcentaje_cambio_dolar / 100)

# Imprimir el DataFrame con los precios actualizados
print("DataFrame con los precios actualizados:")
print(df)

