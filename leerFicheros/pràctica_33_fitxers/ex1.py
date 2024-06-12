"""
Feu un programa que actuï de manera diferent segons si existeix o no una carpeta
anomenada “Temp” a la seva carpeta de treball. Si no existeix, l’ha d’intentar crear. Si
existeix, l’ha d’esborrar. Cada cop que es realitza una acció, cal dir si s’ha pogut dur a
terme i la ruta absoluta de la carpeta processada.
"""
import os
import shutil


def process_temp_folder():
    # Obtenir el directori de treball actual
    current_dir = os.getcwd()

    # Ruta absoluta de la carpeta Temp
    temp_dir = os.path.join(current_dir, 'Temp')

    if os.path.exists(temp_dir):
        try:
            # Intentar esborrar la carpeta
            shutil.rmtree(temp_dir)
            print(f"S'ha esborrat la carpeta {temp_dir}.")
        except Exception as e:
            print(f"No s'ha pogut esborrar la carpeta {temp_dir}. Error: {e}")
    else:
        try:
            # Intentar crear la carpeta
            os.makedirs(temp_dir)
            print(f"S'ha creat la carpeta {temp_dir}.")
        except Exception as e:
            print(f"No s'ha pogut crear la carpeta {temp_dir}. Error: {e}")


# Executar la funció
process_temp_folder()

