from Complejos.formas_complejos.polar import modulo_complejo, fase_complejo


def forma_trigonometrica(parte_real, parte_imaginaria):
    modulo = modulo_complejo(parte_real, parte_imaginaria)

    fase = fase_complejo(parte_real, parte_imaginaria)

    complejo_trigonometrico = str(modulo) + " cos(" + str(fase) + ")" + " + " + str(modulo) \
                              + " sen(" + str(fase) + ")" + "j"

    return complejo_trigonometrico
