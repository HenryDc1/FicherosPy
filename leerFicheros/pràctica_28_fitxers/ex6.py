"""
Exercici 6. Persistència d'un diccionari
Escriure una funció carregar_dades que rebi un nom d'arxiu, el continguºt del
qual té el format clau, valor i retorni un diccionari amb el primer camp com a
clau i el segon com a valor.
Escriure una funció guardar_dades que rebi un diccionari i un nom d'arxiu, i
guardi el contingut del diccionari en l'arxiu, amb el format clau, valor.
"""
def guardar_dades(diccionario, arxiu):
    with open(arxiu, 'w') as archivo:
        for clave, valor in diccionario.items():
            archivo.write(f"{clave}:{valor}\n")

def carregar_dades(arxiu):
    diccionario = {}
    with open(arxiu, 'r') as archivo:
        for linea in archivo:
            clave, valor = linea.strip().split(':')
            diccionario[clave] = valor
    return diccionario

# Ejemplo de uso
datos = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": "30",
    "ciudad": "Madrid"
}

nombre_archivo = 'datos.txt'
guardar_dades(datos, nombre_archivo)
datos_cargados = carregar_dades(nombre_archivo)
print(datos_cargados)
