import math


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

    if complejo_2 != 0:
        return complejo_1 / complejo_2


def potencia(parte_real, parte_im, exponente):
    complejo = complex(parte_real, parte_im)

    if exponente >= 0:
        return complejo ** exponente


# TODO: VER EL OTRO RESULTADO DE LA RAIZ CUADRADA
def raiz_cuadrada(parte_real, parte_im):
    modulo = modulo_complejo(parte_real, parte_im)

    primer_complejo = complex(math.sqrt((modulo + parte_real)/2), math.sqrt((modulo - parte_real)/2))

    return complejo ** (1 / 2)
