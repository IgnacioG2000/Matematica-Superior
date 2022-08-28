import cmath
import math

from Complejos.formas_complejos.polar import modulo_complejo, fase_complejo


def binomica_a_polar(parte_real, parte_imaginaria):
    binomica = complex(parte_real, parte_imaginaria)
    print(f"El complejo en forma binomica es: {binomica}\n")

    polar = cmath.polar(binomica)

    return polar


def polar_a_binomica(modulo, fase):
    fase = fase * math.pi / 180
    binomica = cmath.rect(modulo, fase)

    return binomica
