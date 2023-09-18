import numpy as np
import pandas as pd  # Asegúrate de importar pandas
from datasets import load_dataset

# Cargamos el dataset
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Obtenemos la lista de edades
edades = data["age"]

# Convertimos la lista de edades a un arreglo de NumPy
edades_np = np.array(edades)

# Calculamos el promedio de edad
promedio_edad = np.mean(edades_np)

# Imprimimos el resultado
print(f"El promedio de edad de las personas participantes en el estudio es: {promedio_edad} años")

# Convertimos la estructura Dataset en un DataFrame de Pandas
df = pd.DataFrame(data)

# Separar el DataFrame en dos: uno con personas que fallecieron y otro con el complemento
personas_fallecidas = df[df['is_dead'] == 1]
personas_no_fallecidas = df[df['is_dead'] == 0]

# Calcular el promedio de edades para cada dataset
promedio_edad_fallecidas = personas_fallecidas['age'].mean()
promedio_edad_no_fallecidas = personas_no_fallecidas['age'].mean()

# Imprimir los promedios de edades
print(f"Promedio de edad de personas fallecidas: {promedio_edad_fallecidas:.2f} años")
print(f"Promedio de edad de personas no fallecidas: {promedio_edad_no_fallecidas:.2f} años")

# Verificar los tipos de datos en cada columna
tipos_de_datos = df.dtypes

# Calculamos la cantidad de hombres fumadores y mujeres fumadoras
hombres_fumadores = df[(df['is_male'] == 1) & (df['is_smoker'] == 1)]
mujeres_fumadoras = df[(df['is_male'] == 0) & (df['is_smoker'] == 1)]

# Contamos las filas en cada grupo
cantidad_hombres_fumadores = len(hombres_fumadores)
cantidad_mujeres_fumadoras = len(mujeres_fumadoras)

# Imprimimos los tipos de datos y la cantidad de fumadores por género
print("Tipos de datos en cada columna:")
print(tipos_de_datos)
print("\nCantidad de hombres fumadores:", cantidad_hombres_fumadores)
print("Cantidad de mujeres fumadoras:", cantidad_mujeres_fumadoras)
