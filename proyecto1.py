
#leer el archivo
def leerArchivo():
    with open("BL-Flickr-Images-Book.csv", "r", encoding= "utf-8") as archivo: 
        contenido = archivo.readlines()
        contenidoSinEncabezado = contenido[1:]
        return contenidoSinEncabezado
