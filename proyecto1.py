import re
import pandas as pd
#leer el archivo
def leerArchivo():
    with open("BL-Flickr-Images-Book.csv", "r", encoding= "utf-8") as archivo: 
        contenido = archivo.readlines()
        return contenido
# Usamos la función para leer todo el contenido del archivo
contenido = leerArchivo()

# Tomamos la primera línea del contenido para obtener los encabezados
header_line = contenido[0].strip()

# Usamos una expresión regular para separar los nombres de las columnas por comas
headers = re.findall(r'[^,]+', header_line)

# Aquí es donde vamos a guardar cada fila de datos del archivo, una por una
data = []

# Esta es la expresión regular que nos ayudará a dividir cada línea en campos
# Básicamente busca comas que están al inicio o entre campos y separa valores que están entre comillas o no
pattern = r'(?:,|^)(?:"([^"])"|([^",]))'