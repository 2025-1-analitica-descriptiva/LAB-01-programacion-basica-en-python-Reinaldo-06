"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open('files/input/data.csv', 'r') as f:
        lines = f.readlines()
        lines = [line.split('\t') for line in lines]
    
    claves = sorted(set([item.split(':')[0] for line in lines 
                         for item in line[4].split(',')]))

    contar = {}

    for clave in claves:
        contar[clave] = 0  # inicializar

        for line in lines:
            items = line[4].split(',')

            for item in items:
                clave_actual, valor = item.split(':')
                if clave_actual == clave:
                    contar[clave] += 1


    return contar

