def process_clients_file(filename):
    import os

    # Comprovem si el fitxer existeix
    if not os.path.exists(filename):
        # Si el fitxer no existeix, llencem una excepció de tipus ValueError
        raise ValueError("El fitxer no existeix")

    # Inicialitzem el diccionari per a guardar les dades dels clients
    dadesClients = {}

    # Llegim el fitxer
    with open(filename, 'r') as file:
        lines = file.readlines()  # Llegim totes les línies del fitxer

    # Processar cada línia
    for line in lines:
        # Eliminem espais innecessaris i dividim per punt i coma per obtenir els camps
        fields = [field.strip() for field in line.split(';')]

        # Inicialitzem el diccionari parcial per a guardar les dades d'un client
        diccionariParcial = {}

        # Variables temporals per a cognoms
        surname1, surname2 = None, None

        # Processar cada camp
        for field in fields:
            # Separem la clau i el valor per dos punts
            key, value = field.split(':')
            key = key.strip().lower()  # Eliminem espais innecessaris de la clau i la convertim a minúscules
            value = value.strip()  # Eliminem espais innecessaris del valor

            # Assignem el valor corresponent segons la clau
            if key == 'id':
                client_id = value
            elif key == 'name':
                diccionariParcial['name'] = value
            elif key == 'surnames':
                # Separem els cognoms per guió
                surnames = value.split('-')
                # Assignem el primer i segon cognom
                surname1, surname2 = surnames[0], surnames[1] if len(surnames) > 1 else ''
            elif key == 'dni':
                diccionariParcial['dni'] = value
            elif key == 'tfn':
                diccionariParcial['tfn'] = value
            elif key == 'age':
                diccionariParcial['age'] = value

        # Afegim els cognoms al diccionari parcial
        if surname1 and surname2:
            diccionariParcial['surname1'] = surname1
            diccionariParcial['surname2'] = surname2

        # Afegim el diccionari parcial al diccionari principal amb l'ID del client com a clau
        dadesClients[client_id] = diccionariParcial

    # Mostrem les dades dels clients majors de 18 anys
    # Imprimim les capçaleres de la taula
    print(f"{'ID':<5} {'Name':<15} {'Surname1':<15} {'Surname2':<15} {'DNI':<10} {'TFN':<10} {'Age':<5}")
    print("-" * 80)
    # Recorrem el diccionari de clients
    for client_id, client_data in dadesClients.items():
        # Comprovem si l'edat del client és major o igual a 18
        if int(client_data['age']) >= 18:
            # Imprimim les dades del client
            print(f"{client_id:<5} {client_data['name']:<15} {client_data['surname1']:<15} {client_data['surname2']:<15} {client_data['dni']:<10} {client_data['tfn']:<10} {client_data['age']:<5}")

# Exemple de crida a la funció
try:
    # Cridem a la funció amb el nom del fitxer de clients
    process_clients_file('clients.txt')
except ValueError as e:
    # Captura i mostra el missatge d'error si el fitxer no existeix
    print(e)
