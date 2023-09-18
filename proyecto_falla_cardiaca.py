import numpy as np
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
