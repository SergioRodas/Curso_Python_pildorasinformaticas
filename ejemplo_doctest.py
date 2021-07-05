def area_triangulo(base, altura):

    """
    Calcula el área de un triángulo utilizando los parámetros de base y altura dados.
    Cálculo: (base * altura) /2

    >>> area_triangulo(3, 6)
    'El área del triángulo es: 9.0'

    >>> area_triangulo(4, 5)
    'El área del triángulo es: 10.0'

    >>> area_triangulo(9, 3)
    'El área del triángulo es: 13.5'

    """

    return 'El área del triángulo es: ' + str((base *altura) / 2)


def comprueba_mail(mail_usuario):

    """
    La función comprueba_mail evalúa un mail recibido en busca del @. Si tiene un @ es correcto, si tiene más de un @ o el @ está al final es incorrecto.

    >>> comprueba_mail('sergiorodas@hotmail.com')
    True

    >>> comprueba_mail('sergiorodas@hotmai@l.com')
    False

    >>> comprueba_mail('sergiorodashotmail.com@')
    False

    >>> comprueba_mail('sergiorodashotmail.com')
    False

    """
    arroba = mail_usuario.count('@')
    if arroba != 1 or mail_usuario.rfind('@') == (len(mail_usuario)-1):
        return False
    else: 
        return True

import doctest

doctest.testmod()