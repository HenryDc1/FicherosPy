import os

def create_backup_directory(name):
    # Comprova si s'ha passat un nom vàlid
    if not name:
        raise ValueError("El nom no pot estar buit")

    # Defineix el path de l'arbre de directoris
    base_path = os.path.join(name, 'backups', 'clients')

    # Crea l'arbre de directoris de manera recursiva
    os.makedirs(base_path, exist_ok=True)

    # Mostra un missatge confirmant la creació de l'arbre de directoris
    print(f"Arbre de directoris creat a: {base_path}")

# Exemple de crida a la funció
create_backup_directory('ElTeuCognomElTeuNom')
