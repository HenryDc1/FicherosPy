def llegirPersonesDeDisc(fitxer):
    # Llegeix totes les línies del fitxer
    linies = fitxer.readlines()
    persones = []
    persona = {}

    for linia in linies:
        # Si trobem una línia en blanc, significa que hem acabat de llegir una persona
        if linia.strip() == "":
            if persona:  # Evitem afegir persones buides
                persones.append(persona)
                persona = {}
        else:
            # Extraiem la clau i el valor de la línia
            clau, valor = linia.split(": ")
            persona[clau.strip()] = valor.strip()

    # Afegeix l'última persona si existeix
    if persona:
        persones.append(persona)

    return persones


def mostrarMajorsDe18(persones):
    for persona in persones:
        if int(persona['Edat']) > 18:
            print("Nom:", persona['Nom'])
            print("Cognoms:", persona['Cognoms'])
            print("NIF:", persona['NIF'])
            print("Edat:", persona['Edat'])
            print("Alzada:", persona['Alzada'])
            print()  # Línia en blanc per separar persones


def main():
    # Obrim l'arxiu "persones.txt" en mode lectura
    with open("persones.txt", "r") as fitxer:
        persones = llegirPersonesDeDisc(fitxer)

    # Mostrem les dades de les persones majors de 18 anys
    mostrarMajorsDe18(persones)


if __name__ == "__main__":
    main()
