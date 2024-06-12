"""
Exercici 3.
Escriure un programa que donat un arxiu de text, un delimitador, i una llista de
camps, imprimeixi solament aquests camps, separats per aquest delimitador.
"""
def imprimir_campos(arxiu, delimitador, campos):
    try:
        with open(arxiu, 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split(delimitador)
                campos_seleccionados = [partes[i] for i in campos if i < len(partes)]
                print(delimitador.join(campos_seleccionados))
    except Exception as e:
        print("Error al procesar el archivo:", e)

imprimir_campos('agenda.txt', ',', [0, 2, 3])

