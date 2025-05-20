"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/input/data.csv', 'r') as f:
        lines = f.readlines()
        lines = [line.split('\t') for line in lines]

    contar = [
        (
            letter,
            max(int(line[1]) for line in lines if line[0] == letter),
            min(int(line[1]) for line in lines if line[0] == letter)
        )
        for letter in sorted(set(line[0] for line in lines))
    ]
    return contar

print(pregunta_05())