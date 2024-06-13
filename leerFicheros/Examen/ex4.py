import os
import shutil

def backup_client_file(client_file, name):
    # Comprova si el fitxer de clients existeix
    if not os.path.exists(client_file):
        raise ValueError("El fitxer de clients no existeix")

    # Comprova si s'ha passat un nom vàlid
    if not name:
        raise ValueError("El nom no pot estar buit")

    # Defineix el path de l'arbre de directoris de backup
    backup_directory = os.path.join(name, 'backups', 'clients')

    # Crea l'arbre de directoris de manera recursiva si no existeix
    os.makedirs(backup_directory, exist_ok=True)

    # Defineix el path del fitxer de backup
    backup_file_path = os.path.join(backup_directory, os.path.basename(client_file))

    # Realitza una còpia del fitxer de clients al directori de backup
    shutil.copy2(client_file, backup_file_path)

    # Mostra un missatge confirmant la còpia del fitxer
    print(f"Còpia del fitxer de clients realitzada a: {backup_file_path}")

# Exemple de crida a la funció
try:
    backup_client_file('clients.txt', 'ElTeuCognomElTeuNom')
except ValueError as e:
    print(e)
