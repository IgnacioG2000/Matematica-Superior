import math

from Complejos.formas_complejos.polar import modulo_complejo, forma_polar, fase_complejo


def suma_complejos(parte_real_1, parte_im_1, parte_real_2, parte_im_2):
    complejo_1 = complex(parte_real_1, parte_im_1)
    complejo_2 = complex(parte_real_2, parte_im_2)

    return complejo_1 + complejo_2


def resta_complejos(parte_real_1, parte_im_1, parte_real_2, parte_im_2):
    complejo_1 = complex(parte_real_1, parte_im_1)
    complejo_2 = complex(parte_real_2, parte_im_2)

    return complejo_1 - complejo_2


def multiplicacion(parte_real_1, parte_im_1, parte_real_2, parte_im_2):
    complejo_1 = complex(parte_real_1, parte_im_1)
    complejo_2 = complex(parte_real_2, parte_im_2)

    return complejo_1 * complejo_2


def division(parte_real_1, parte_im_1, parte_real_2, parte_im_2):
    complejo_1 = complex(parte_real_1, parte_im_1)
    complejo_2 = complex(parte_real_2, parte_im_2)

    if complejo_2 != 0j:
        return complejo_1 / complejo_2
    else:
        raise ZeroDivisionError("Estas dividiendo por 0")


def potencia(parte_real, parte_im, exponente):
    complejo = complex(parte_real, parte_im)

    if exponente >= 0:
        return complejo ** exponente


def raiz_cuadrada(parte_real, parte_im):
    modulo = modulo_complejo(parte_real, parte_im)

    if parte_im >= 0:
        primer_complejo = complex(round(math.sqrt((modulo + parte_real) / 2), 3),
                                  round(math.sqrt((modulo - parte_real) / 2), 3))

        segundo_complejo = complex(round((-1) * math.sqrt((modulo + parte_real) / 2), 3),
                                   round((-1) * math.sqrt((modulo - parte_real) / 2), 3))
        return primer_complejo, segundo_complejo
    else:
        primer_complejo = complex(round((-1) * math.sqrt((modulo + parte_real) / 2), 3),
                                  round(math.sqrt((modulo - parte_real) / 2), 3))
        segundo_complejo = complex(round(math.sqrt((modulo + parte_real) / 2), 3),
                                   round((-1) * math.sqrt((modulo - parte_real) / 2), 3))
        return primer_complejo, segundo_complejo


def logaritmo_natural_complejo(complejo):
    modulo = modulo_complejo(complejo.real, complejo.imag)
    fase = fase_complejo(complejo.real, complejo.imag)

    return "ln (" + str(modulo) + ")" + " + " + "j * " + str(fase)


def bhaskara(a, b, c):
    discriminante = b ** 2 - 4 * a * c
    raiz1, raiz2 = raiz_cuadrada(discriminante.real, discriminante.imag)
    resultado1 = ((-1) * b + raiz1) / (2 * a)
    resultado2 = ((-1) * b + raiz2) / (2 * a)
    return resultado1, resultado2
