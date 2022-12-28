import math

from Complejos.calculos.transformaciones import polar_a_binomica, binomica_a_polar
from Complejos.formas_complejos.polar import modulo_complejo, fase_complejo


def suma_complejos(complejo_1, complejo_2):
    return complejo_1 + complejo_2


def resta_complejos(complejo_1, complejo_2):
    return complejo_1 - complejo_2


def multiplicacion(complejo_1, complejo_2):
    return complejo_1 * complejo_2


def division(complejo_1, complejo_2):
    if complejo_2 != 0j:
        return complejo_1 / complejo_2
    else:
        raise ZeroDivisionError("Estas dividiendo por 0")


def potencia(complejo, exponente):
    if exponente >= 0:
        return complejo ** exponente


def raiz_cuadrada(complejo):
    modulo = modulo_complejo(complejo.real, complejo.imag)

    if complejo.imag >= 0:
        primer_complejo = complex(round(math.sqrt((modulo + complejo.real) / 2), 3),
                                  round(math.sqrt((modulo - complejo.real) / 2), 3))

        segundo_complejo = complex(round((-1) * math.sqrt((modulo + complejo.real) / 2), 3),
                                   round((-1) * math.sqrt((modulo - complejo.real) / 2), 3))
        return primer_complejo, segundo_complejo
    else:
        primer_complejo = complex(round((-1) * math.sqrt((modulo + complejo.real) / 2), 3),
                                  round(math.sqrt((modulo - complejo.real) / 2), 3))
        segundo_complejo = complex(round(math.sqrt((modulo + complejo.real) / 2), 3),
                                   round((-1) * math.sqrt((modulo - complejo.real) / 2), 3))
        return primer_complejo, segundo_complejo


def logaritmo_natural_complejo(complejo):
    modulo = modulo_complejo(complejo.real, complejo.imag)
    fase = fase_complejo(complejo.real, complejo.imag)

    return "ln (" + str(modulo) + ")" + " + " + "j * " + str(fase)


def bhaskara(a, b, c):
    discriminante = b ** 2 - 4 * a * c
    raiz1, raiz2 = raiz_cuadrada(discriminante)
    resultado1 = ((-1) * b + raiz1) / (2 * a)
    resultado2 = ((-1) * b + raiz2) / (2 * a)
    return resultado1, resultado2


def suma_funciones_por_fasores(modulo1, fase1, tipo_senial1, modulo2, fase2, tipo_senial2, frecuencia, opcion_muestra):
    resultado_fase = ""
    fase1 = math.radians(fase1)
    fase2 = math.radians(fase2)
    if tipo_senial1 != tipo_senial2:
        if opcion_muestra == 'sen':
            if tipo_senial1 == 'cos':
                fase1 += math.pi / 2
            elif tipo_senial2 == 'cos':
                fase2 += math.pi / 2
        else:
            if tipo_senial1 == 'sen':
                fase1 -= math.pi / 2
            elif tipo_senial2 == 'sen':
                fase2 -= math.pi / 2

    binomica_1 = polar_a_binomica(modulo1, fase1)
    binomica_2 = polar_a_binomica(modulo2, fase2)

    suma_fasores = suma_complejos(binomica_1, binomica_2)

    resultado = binomica_a_polar(suma_fasores.real, suma_fasores.imag)

    if resultado[1] >= 0:
        resultado_fase = "+" + str(resultado[1])
        return str(resultado[0]) + opcion_muestra + "(" + str(frecuencia) + "t" + str(resultado_fase) + ")"
    else:
        return str(resultado[0]) + opcion_muestra + "(" + str(frecuencia) + "t" + str(resultado[1]) + ")"
