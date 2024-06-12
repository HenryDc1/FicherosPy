import os
import shutil

# Pas 1: Crear l'estructura de directoris
os.makedirs('exercicis/Data/operacions', exist_ok=True)

# Pas 2: Escriure dades del pacient a pacients.txt
pacient = {'nom': 'Pep', 'edat': 42, 'Diabetic': True}
file_path = 'exercicis/Data/operacions/pacients.txt'

with open(file_path, 'a') as f:
    f.write(f"{pacient['nom']}\t{pacient['edat']}\t{pacient['Diabetic']}\n")

# Pas 3: Fer una còpia de seguretat de l'estructura de directoris
src_dir = 'exercicis/Data/operacions'
backup_dir = 'exercicis/Data/backup_operacions'
shutil.copytree(src_dir, backup_dir)

# Pas 4: Copiar pacients.txt a la carpeta data
os.makedirs('exercicis/data', exist_ok=True)
src_file = 'exercicis/Data/operacions/pacients.txt'
dst_file = 'exercicis/data/pacients.txt'
shutil.copy(src_file, dst_file)

# Pas 5: Eliminar l'arxiu del directori original
os.remove(src_file)
