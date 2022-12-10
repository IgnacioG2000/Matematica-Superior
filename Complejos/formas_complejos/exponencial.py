from Complejos.formas_complejos.polar import modulo_complejo, fase_complejo


def forma_exponencial(parte_real, parte_imaginaria):
    # modulo * e^jfi
    modulo = modulo_complejo(parte_real, parte_imaginaria)

    fase = fase_complejo(parte_real, parte_imaginaria)

    complejo_exponencial = str(modulo) + " * e^(j*" + str(fase) + ")"

    return complejo_exponencial
