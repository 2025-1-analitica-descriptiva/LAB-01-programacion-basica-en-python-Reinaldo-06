"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open('files/input/data.csv', 'r') as f:
        lines = f.readlines()
        lines = [line.strip().split('\t') for line in lines]
    
    claves = sorted(set(line[0] for line in lines))

    contar = {}

    for clave in claves:
        contar[clave] = 0

        for line in lines:
            items = line[4].split(',')

            for item in items:
                _, valor =item.split(':')

                if clave == line[0]:

                    contar[clave] += int(valor)
    
    return contar

print(pregunta_12())


