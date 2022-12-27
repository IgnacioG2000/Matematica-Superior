from flask import render_template

from Complejos.calculos.operaciones import suma_complejos, resta_complejos, multiplicacion, division
from Complejos.formas_complejos.binomica import forma_binomica
from Complejos.formas_complejos.exponencial import forma_exponencial
from Complejos.formas_complejos.polar import forma_polar
from Complejos.formas_complejos.trigonometrica import forma_trigonometrica


def realizar_operacion_segun_operador(complejo1, complejo2, operador, template):
    if operador == 'suma':
        complejo_suma = suma_complejos(complejo1, complejo2)
        return render_template(template, complejo=complejo_suma, operacion=operador)
    elif operador == 'resta':
        complejo_resta = resta_complejos(complejo1, complejo2)
        return render_template(template, complejo=complejo_resta, operacion=operador)
    elif operador == 'multiplicacion':
        complejo_multiplicacion = multiplicacion(complejo1, complejo2)
        return render_template(template, complejo=complejo_multiplicacion, operacion=operador)
    else:
        complejo_cociente = division(complejo1, complejo2)
        return render_template(template, complejo=complejo_cociente, operacion=operador)


def mostrar_complejo_segun_opcion(parte_real, parte_imaginaria, opcion, template):
    if opcion == 'binomica':
        complejo_binomica = forma_binomica(parte_real, parte_imaginaria)
        return render_template(template, complejo=complejo_binomica, operacion=opcion)
    elif opcion == 'exponencial':
        complejo_exponencial = forma_exponencial(parte_real, parte_imaginaria)
        return render_template(template, complejo=complejo_exponencial, operacion=opcion)
    elif opcion == 'trigonometrica':
        complejo_trigonometrica = forma_trigonometrica(parte_real, parte_imaginaria)
        return render_template(template, complejo=complejo_trigonometrica, operacion=opcion)
    else:
        complejo_polar = forma_polar(parte_real, parte_imaginaria)
        return render_template(template, complejo=complejo_polar, operacion=opcion)
