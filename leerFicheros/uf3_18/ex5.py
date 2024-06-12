def main():
    # Especifiquem els noms dels arxius
    arxiu1 = 'arxiu1.txt'
    arxiu2 = 'arxiu2.txt'

    # Llegeix totes les línies de l'arxiu 1
    with open(arxiu1, 'r') as fitxer1:
        linies_arxiu1 = fitxer1.readlines()

    # Llegeix els números de línia de l'arxiu 2 i converteix-los a enters
    with open(arxiu2, 'r') as fitxer2:
        numeros_de_linia = [int(linia.strip()) for linia in fitxer2 if linia.strip()]

    # Mostra les línies de l'arxiu 1 corresponents als números de l'arxiu 2
    for numero in numeros_de_linia:
        if 1 <= numero <= len(linies_arxiu1):  # Comprova que el número de línia és vàlid
            print(linies_arxiu1[numero - 1].strip())


if __name__ == "__main__":
    main()
