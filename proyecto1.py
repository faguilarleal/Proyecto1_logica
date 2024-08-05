import re
import pandas as pd
from pandasgui import show

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

# Imprimir los encabezados para verificar
print("Encabezados extraídos:", headers)

# Aquí es donde vamos a guardar cada fila de datos del archivo, una por una
data = []

# Esta es la expresión regular que nos ayudará a dividir cada línea en campos
# Básicamente busca comas que están al inicio o entre campos y separa valores que están entre comillas o no
pattern = r'(?:^|,)(?:"([^"]*)"|([^",]*))'

# Ahora recorremos cada línea del contenido a partir de la segunda (ya que la primera es el encabezado)
for line in contenido[1:]:
    # Limpiamos la línea actual para que no tenga espacios ni saltos de línea al final
    line = line.strip()
    
    # Usamos la expresión regular para dividir la línea en sus campos y obtenerlos como pares de coincidencias
    # Cada campo de la línea se procesa y se captura con la expresión regular
    matches = re.findall(pattern, line)
    
    # Creamos una lista 'row' que contiene cada valor de la línea actual
    # Elegimos el valor correcto si hay comillas o no, gracias a la magia de la expresión regular
    row = [match[0] if match[0] else match[1] for match in matches]
    
    # Verificamos que el número de columnas coincida con el de los encabezados
    # Si no coincide, añadimos columnas vacías para que todo cuadre bien
    row = row[:len(headers)] + [''] * (len(headers) - len(row))
    
    # Añadimos la fila procesada a nuestra lista de datos
    data.append(row)

# Transferir los datos a un DataFrame
df = pd.DataFrame(data, columns=headers)

# Imprimir el DataFrame para verificar
print("DataFrame creado:")
print(df.head())

# Asignar tipos de datos específicos a cada columna según los encabezados reales
column_types = {
    'Identifier': 'int',
    'Edition Statement': 'string',
    'Place of Publication': 'string',
    'Date of Publication': 'Int64',  
    'Publisher': 'string',
    'Title': 'string',
    'Author': 'string',
    'Contributors': 'string',
    'Corporate Author': 'string',
    'Corporate Contributors': 'string',
    'Former owner': 'string',
    'Engraver': 'string',
    'Issuance type': 'string',
    'Flickr URL': 'string',
    'Shelfmarks': 'string'
}

# Mostrar el DataFrame con pandasgui
show(df)
