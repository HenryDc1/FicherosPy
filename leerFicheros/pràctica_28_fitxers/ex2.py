#Escriure un programa que copiï tot el contingut d'un arxiu (sigui de text o binari) a un altre, de manera que quedi exactament igual.
#Nota: Utilitzar la funció read(Numbytes) per llegir com a màxim una quantitatde bytes
with open('copiar.txt', "rb") as a1 , open('copiar2.txt', "wb") as a2:
    while True:
        c = a1.read(1024)  # Leer un fragmento de máximo 1024 bytes
        if not c:  # Si no hay más datos para leer, salir del bucle
            break
        a2.write(c)  # Escribir el fragmento en el archivo de destino

