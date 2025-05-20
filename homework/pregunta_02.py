"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open('files/input/data.csv', 'r') as f:
        lines = f.readlines()
        lines = [line.split('\t') for line in lines]

    contar = [(letter,sum(1 for line in lines if line[0]==letter)) for letter in set(line[0] for line in lines)]
    contar.sort(key=lambda x:x[0])

    # Contar la cantidad de registros por cada letra
    #counts = {}
    #for line in lines:
    #    letter = line[0]
    #    if letter in counts:
    #        counts[letter] += 1
    #    else:
    #        counts[letter] = 1
    #
    ## Convertir el diccionario a una lista de tuplas
    #counts_list = [(letter, count) for letter, count in counts.items()]
    #print(counts_list)

    return contar
