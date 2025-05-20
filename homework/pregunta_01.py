"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    
    Rta/
    214

    
    """
    with open('files/input/data.csv', 'r') as f:
        lines = f.readlines()
        lines = [line.split('\t') for line in lines]
    suma=0
    for i in range(len(lines)):
        suma += int(lines[i][1])
    
    return suma


