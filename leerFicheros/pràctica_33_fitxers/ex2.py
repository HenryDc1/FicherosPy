"""
L’objectiu d’aquesta activitat és veure com canviar el nom a un conjunt de fitxers.
Genereu un programa que pregunti a l’usuari dues cadenes de text de tres lletres, de
manera que les pugui escriure pel teclat en una mateixa línia. El programa ha de cercar
tots els fitxers en el seu directori de treball que tinguin com extensió la primera cadena
de text i canviar-la a la segona. Per exemple, si l’usuari escriu “txt jpg”, tots els fitxers
amb extensió ”.txt” han de passar a tenir l’extensió ”.jpg”.
"""
import os


def canvia_extensions(extensio_vella, extensio_nova):
    # Obtenir el directori de treball actual
    current_dir = os.getcwd()

    # Llistar tots els fitxers al directori de treball actual
    for filename in os.listdir(current_dir):
        # Comprovar si el fitxer té l'extensió antiga
        if filename.endswith(f".{extensio_vella}"):
            # Construir el nou nom del fitxer amb la nova extensió
            base = os.path.splitext(filename)[0]
            nou_nom = f"{base}.{extensio_nova}"

            # Canviar el nom del fitxer
            os.rename(filename, nou_nom)
            print(f"S'ha canviat {filename} a {nou_nom}")


# Preguntar a l'usuari les dues cadenes de text
extensio_vella, extensio_nova = input(
    "Introdueix dues cadenes de text de tres lletres separades per un espai: ").split()

# Cridar la funció per canviar les extensions
canvia_extensions(extensio_vella, extensio_nova)
