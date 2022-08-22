from Complejos.grafico import dibujar_complejos

parte_real = float(input("Digita la parte real del complejo: "))
parte_imaginaria = float(input("Digita la parte imaginaria del complejo: "))

complejo = complex(parte_real, parte_imaginaria)

print(complejo)
dibujar_complejos(complejo)
