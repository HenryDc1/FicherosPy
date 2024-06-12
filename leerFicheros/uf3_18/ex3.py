def llegirPersona():
    # Llegim les dades de la persona
    nom = input("Introdueix el nom: ")
    cognoms = input("Introdueix els cognoms: ")
    nif = input("Introdueix el NIF: ")
    edat = input("Introdueix l'edat: ")
    alcada = input("Introdueix l'alzada (en metres, p.ex: 1.63): ")
    # Retornem les dades com una llista
    return [nom, cognoms, nif, edat, alcada]

def escriurePersonaADisc(persona, fitxer):
    # Escriu les dades de la persona a l'arxiu
    fitxer.write(f"Nom: {persona[0]}\n")
    fitxer.write(f"Cognoms: {persona[1]}\n")
    fitxer.write(f"NIF: {persona[2]}\n")
    fitxer.write(f"Edat: {persona[3]}\n")
    fitxer.write(f"Alzada: {persona[4]}\n")
    fitxer.write("\n")

def main():
    # Obrim l'arxiu "persones.txt" en mode escriptura
    with open("persones.txt", "a") as fitxer:
        while True:
            # Llegim les dades d'una persona
            persona = llegirPersona()
            # Escriu les dades de la persona a l'arxiu
            escriurePersonaADisc(persona, fitxer)
            # Preguntem si volen introduir més persones
            continuar = input("Vols introduir una altra persona? (sí/no): ").strip().lower()
            if continuar != 'sí':
                break

if __name__ == "__main__":
    main()
