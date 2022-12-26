import cmath


def binomica_a_polar(parte_real, parte_imaginaria):
    binomica = complex(parte_real, parte_imaginaria)
    print(f"El complejo en forma binomica es: {binomica}\n")

    polar = cmath.polar(binomica)

    return polar


def polar_a_binomica(modulo, fase):
    binomica = cmath.rect(modulo, fase)

    return binomica
