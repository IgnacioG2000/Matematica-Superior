from Complejos.formas_complejos.binomica import forma_binomica
from Complejos.formas_complejos.polar import *
from Complejos.grafico import dibujar_complejos

parte_real = float(input("Digita la parte real del complejo_binomica: "))
parte_imaginaria = float(input("Digita la parte imaginaria del complejo_binomica: "))

complejo_binomica = forma_binomica(parte_real, parte_imaginaria)
modulo_complejo = modulo_complejo(parte_real, parte_imaginaria)
fase_complejo = fase_complejo(parte_real, parte_imaginaria)
complejo_polar = forma_polar(parte_real, parte_imaginaria)

print(f"El complejo en forma binomica es: {complejo_binomica}\n")
print(f"El modulo del complejo es: {modulo_complejo}")
print(f"La fase del complejo es: {fase_complejo}")
print(f"El complejo en forma polar es: {complejo_polar}")
dibujar_complejos(complejo_binomica)
