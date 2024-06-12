import codecs

def cifrar_texto(origen, destino):
    try:
        with open(origen, 'r') as archivo_origen:
            with open(destino, 'w') as archivo_destino:
                for linea in archivo_origen:
                    linea_cifrada = codecs.encode(linea, 'rot_13')
                    archivo_destino.write(linea_cifrada)
    except Exception as e:
        print("Error al procesar el archivo:", e)

cifrar_texto('copiar.txt', 'nuevo_archivo.txt')
