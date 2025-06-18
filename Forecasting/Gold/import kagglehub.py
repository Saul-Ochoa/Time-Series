import kagglehub
import shutil
import os

# Descargar el dataset
path_temp = kagglehub.dataset_download("franciscogcc/financial-data")

# Carpeta destino donde quieres guardar el dataset
path_final = r"D://Github-Time//Time-Series//Forecasting//Gold"
os.makedirs(path_final, exist_ok=True)

# Copiar todos los archivos descargados a la carpeta final
for archivo in os.listdir(path_temp):
    ruta_origen = os.path.join(path_temp, archivo)
    ruta_destino = os.path.join(path_final, archivo)
    shutil.copy2(ruta_origen, ruta_destino)

print(f"✅ Archivos copiados a: {path_final}")
