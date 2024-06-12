"""
L’objectiu d’aquesta activitat és saber recórrer una jerarquia de carpetes i fitxers per
realitzar operacions sobre ella.
Feu un programa que pregunti per pantalla el nom d’un fitxer i el text de la ruta a una
carpeta. Aquestes dades les introduirà l’usuari pel teclat. Llavors el programa ha de
cercar i mostrar per pantalla la ruta absoluta de tots els fitxers amb aquest nom a partir
de la carpeta assenyalada (tant directament dintre seu com dins d’altres carpetes
successives).
Pista: una solució recursiva pot ser més senzilla.
"""
import os


def buscar_fitxers(nom_fitxer, carpeta):
    # Llista per emmagatzemar les rutes trobades
    resultats = []

    # Funció recursiva per cercar el fitxer
    def cercar(carpeta_actual):
        # Recorre tots els elements dins de la carpeta actual
        for element in os.listdir(carpeta_actual):
            # Obtenim la ruta completa de l'element
            ruta_completa = os.path.join(carpeta_actual, element)

            # Comprovem si l'element és una carpeta
            if os.path.isdir(ruta_completa):
                # Crida recursiva a la funció per a la carpeta
                cercar(ruta_completa)
            elif os.path.isfile(ruta_completa) and element == nom_fitxer:
                # Si és un fitxer i el nom coincideix, afegim a la llista de resultats
                resultats.append(ruta_completa)

    # Iniciar la cerca des de la carpeta especificada
    cercar(carpeta)

    # Retornar els resultats trobats
    return resultats


# Preguntar a l'usuari les dades
nom_fitxer = input("Quin és el nom del fitxer a cercar? ")
carpeta = input("Escriu el nom d'una ruta a una carpeta: ")

# Cercar els fitxers
resultats = buscar_fitxers(nom_fitxer, carpeta)

# Mostrar els resultats
if resultats:
    for resultat in resultats:
        print(f"S'ha trobat el fitxer a: {resultat}")
else:
    print("No s'ha trobat cap fitxer amb aquest nom.")
