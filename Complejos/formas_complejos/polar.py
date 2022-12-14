import cmath
import math


def forma_polar(parte_real, parte_imaginaria):
    polar_complejo = cmath.polar(complex(parte_real, parte_imaginaria))
    return polar_complejo


def modulo_complejo(parte_real, parte_imaginaria):
    modulo = round(math.sqrt(abs(parte_real) ** 2 + abs(parte_imaginaria) ** 2), 3)
    return modulo


def fase_complejo(parte_real, parte_imaginaria):
    fase = round(cmath.phase(complex(parte_real, parte_imaginaria)), 3)
    return fase
