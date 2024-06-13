import random
import string

def generate_unique_id(existing_ids):
    # Aquesta funció genera un ID únic compost per dues lletres i un número.
    # Comprova que el nou ID no estigui ja en la llista d'IDs existents.

    while True:
        # Generem dues lletres aleatòries
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        # Generem un número aleatori entre 0 i 9
        number = str(random.randint(0, 9))
        # Combinem les lletres i el número per formar l'ID
        new_id = letters + number
        # Si l'ID no existeix en la llista d'IDs existents, el retornem
        if new_id not in existing_ids:
            return new_id

def add_client_to_file(client_dict, filename):
    import os

    # Comprovem si el fitxer existeix. Si no, llencem una excepció
    if not os.path.exists(filename):
        raise ValueError("El fitxer no existeix")

    # Llegim les dades existents del fitxer per obtenir els IDs existents
    existing_ids = set()  # Utilitzem un conjunt per emmagatzemar els IDs existents
    with open(filename, 'r') as file:
        lines = file.readlines()  # Llegim totes les línies del fitxer
        for line in lines:
            for field in line.split(';'):  # Separem cada camp per punt i coma
                key, value = [x.strip() for x in field.split(':')]  # Separem la clau i el valor per dos punts
                if key == 'id':  # Si la clau és 'id', afegim l'ID al conjunt d'IDs existents
                    existing_ids.add(value)

    # Generem un ID únic per al nou client
    new_id = generate_unique_id(existing_ids)
    # Afegim l'ID generat al diccionari del nou client
    client_dict['id'] = new_id

    # Formatem les dades del nou client segons el format especificat
    client_line = f"Name: {client_dict['name']}; id: {client_dict['id']} ; surnames: {client_dict['surname1']}-{client_dict['surname2']}; age: {client_dict['age']}; dni: {client_dict['dni']}; tfn: {client_dict['tfn']}\n"

    # Afegim el nou client al fitxer obrint-lo en mode append ('a')
    with open(filename, 'a') as file:
        file.write(client_line)  # Escriu la línia del nou client al fitxer

# Exemple de diccionari de client
dictClient = {'name': 'Sebastian', 'surname1': 'Almansa', 'surname2': 'Navarro', 'dni': '77777777G', 'tfn': '767676767', 'age': '34'}

# Exemple de crida a la funció
try:
    add_client_to_file(dictClient, 'clients.txt')
except ValueError as e:
    # Captura i mostra el missatge d'error si el fitxer no existeix
    print(e)
