#Escriure un programa, que rebi un arxiu i un nombre N i imprimeixi les primeres N línies de l'arxiu.
def impr(arxiu, n):
    with open(arxiu, "r") as archivo:
        for i in range(n):
            linea = archivo.readline()  # Leer una línea del archivo
            print(linea)  # Imprimir la línea sin agregar una nueva línea

# Llamar a la función con el nombre del archivo y el número de líneas a imprimir
impr('lineas.txt', 4)  # Por ejemplo, imprimir las primeras 5 líneas
