"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabéticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    with open('files/input/data.csv', 'r') as f:
        lines = f.readlines()
        lines = [line.strip().split('\t') for line in lines]

    resultado = {}

    for line in lines:
        valor = int(line[1])  # columna 2
        letras = line[3].split(',')  # columna 4 (letras separadas por coma)

        for letra in letras:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += valor

    return dict(sorted(resultado.items()))
