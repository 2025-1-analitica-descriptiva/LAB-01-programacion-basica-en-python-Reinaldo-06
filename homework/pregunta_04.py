"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    with open('files/input/data.csv', 'r') as f:
        lines = f.readlines()
        lines = [line.split('\t') for line in lines]

    meses = ['{:02d}'.format(i) for i in range(1, 13)]
    contar = [(month, sum(1 for line in lines if line[2][5:7] == month)) for month in meses]
    contar.sort(key=lambda x:x[0])
    return contar


pregunta_04()

