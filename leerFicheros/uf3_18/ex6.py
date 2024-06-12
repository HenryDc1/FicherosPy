# Parte a) Escribir el contenido en el archivo
with open('arxiu.txt', 'w') as archivo:
    contenido = """All paid jobs absorb and degrade the mind.
If Beethoven had been killed in a plane crash at the age of 22, it would have changed
the history of music... and of aviation.
I do not have a psychiatrist and I do not want one, for the simple reason that if he
listened to me long enough, he might become disturbed."""
    archivo.write(contenido)

# Parte b) Leer y mostrar la primera frase del archivo
with open('arxiu.txt', 'r') as archivo:
    primera_frase = archivo.readline()
    print("Primera frase del archivo:")
    print(primera_frase)

# Parte c) Mostrar la palabra "mind" desde la posición inicial
with open('arxiu.txt', 'r') as archivo:
    primera_frase = archivo.readline()
    posicion_mind = primera_frase.find("mind")
    print("La palabra 'mind' está en la posición:", posicion_mind)

# Parte e) Mostrar la palabra "Beethoven" desde la posición actual
with open('arxiu.txt', 'r') as archivo:
    archivo.readline()  # Saltar la primera línea
    segunda_frase = archivo.readline()
    posicion_beethoven = segunda_frase.find("Beethoven")
    print("La palabra 'Beethoven' está en la posición:", posicion_beethoven)

# Parte g) Mostrar la última frase
with open('arxiu.txt', 'r') as archivo:
    lineas = archivo.readlines()
    ultima_frase = lineas[-1].strip()
    print("Última frase del archivo:")
    print(ultima_frase)

# Parte h) Calcular el tamaño del archivo en KBytes
import os
tamano = os.path.getsize('arxiu.txt') / 1024  # Convertir bytes a KBytes
print("El tamaño del archivo es:", tamano, "KBytes")
