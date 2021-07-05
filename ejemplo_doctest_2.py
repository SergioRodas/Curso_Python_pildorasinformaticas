import math

def raiz_cuadrada(lista_de_numeros):
    """
    
    La función devuelve una lista con la raíz cuadrada de los elementos numéricos pasados por parámetros en otra lista

    >>> lista = []
    >>> for i in [4, 9, 16]:
    ...     lista.append(i)    # Para anidar e indicar indentación se aplican '...'
    >>> raiz_cuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista = []
    >>> for i in [4, -9, 16, -90, 123]:
    ...     lista.append(i)
    >>> raiz_cuadrada(lista)
    Traceback (most recent call last):
        ...          # Mientras que la primera y la última línea del error sean correctas es suficiente, los '...' indican que el contenido del medio puede variar
    ValueError: math domain error
    
    """


    return [math.sqrt(n) for n in lista_de_numeros]

# print(raiz_cuadrada([9, -16, 25, 36]))

import doctest
doctest.testmod()

    