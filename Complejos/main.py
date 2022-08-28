from Complejos.formas_complejos.binomica import forma_binomica
from Complejos.formas_complejos.polar import *
from Complejos.grafico import dibujar_complejos
from Complejos.calculos.operaciones import *
from Complejos.menu import menu
import sys as s

seguir_programa = ""

iniciar_programa = input("Desea iniciar el programa (S/N): ").upper()
if iniciar_programa == "S":
    while seguir_programa != "N":
        menu()
        opcion = int(input("\nIngresa la opcion deseada: "))

        if opcion == 1:
            parte_real = float(input("\nDigita la parte real del complejo: "))
            parte_imaginaria = float(input("Digita la parte imaginaria del complejo: "))

            binomica = forma_binomica(parte_real, parte_imaginaria)
            print("Forma binomica: {0:.3f}".format(binomica))

        elif opcion == 2:
            parte_real = float(input("\nDigita la parte real del complejo: "))
            parte_imaginaria = float(input("Digita la parte imaginaria del complejo: "))

            polar = forma_polar(parte_real, parte_imaginaria)
            print(f"Forma polar: {polar}")

        elif opcion == 3:
            parte_real_1 = float(input("\nDigita la parte real del complejo 1: "))
            parte_imaginaria_1 = float(input("Digita la parte imaginaria del complejo 1: "))
            parte_real_2 = float(input("Digita la parte real del complejo 2: "))
            parte_imaginaria_2 = float(input("Digita la parte imaginaria del complejo 2: "))

            suma = suma(parte_real_1, parte_imaginaria_1, parte_real_2, parte_imaginaria_2)
            print("Suma = {0:.3f}".format(suma))

        elif opcion == 4:
            parte_real_1 = float(input("\nDigita la parte real del complejo 1: "))
            parte_imaginaria_1 = float(input("Digita la parte imaginaria del complejo 1: "))
            parte_real_2 = float(input("Digita la parte real del complejo 2: "))
            parte_imaginaria_2 = float(input("Digita la parte imaginaria del complejo 2: "))

            resta = resta(parte_real_1, parte_imaginaria_1, parte_real_2, parte_imaginaria_2)
            print("Resta = {0:.3f}".format(resta))

        elif opcion == 5:
            parte_real_1 = float(input("\nDigita la parte real del complejo 1: "))
            parte_imaginaria_1 = float(input("Digita la parte imaginaria del complejo 1: "))
            parte_real_2 = float(input("Digita la parte real del complejo 2: "))
            parte_imaginaria_2 = float(input("Digita la parte imaginaria del complejo 2: "))

            producto = multiplicacion(parte_real_1, parte_imaginaria_1, parte_real_2, parte_imaginaria_2)
            print("Producto = {0:.3f}".format(producto))

        elif opcion == 6:
            parte_real_1 = float(input("\nDigita la parte real del complejo 1: "))
            parte_imaginaria_1 = float(input("Digita la parte imaginaria del complejo 1: "))
            parte_real_2 = float(input("Digita la parte real del complejo 2: "))
            parte_imaginaria_2 = float(input("Digita la parte imaginaria del complejo 2: "))

            cociente = division(parte_real_1, parte_imaginaria_1, parte_real_2, parte_imaginaria_2)
            print("{0:.3f}".format(cociente))

        elif opcion == 7:
            parte_real = float(input("\nDigita la parte real del complejo: "))
            parte_imaginaria = float(input("Digita la parte imaginaria del complejo: "))
            exponente = float(input("Digita el exponente: "))

            resultado = potencia(parte_real, parte_imaginaria, exponente)
            print("{0:.3f}".format(resultado))

        elif opcion == 8:
            parte_real = float(input("\nDigita la parte real del complejo: "))
            parte_imaginaria = float(input("Digita la parte imaginaria del complejo: "))

            resultado = raiz_cuadrada(parte_real, parte_imaginaria)
            print("{0:.3f}".format(resultado))

        elif opcion == 9:
            parte_real = float(input("\nDigita la parte real del complejo: "))
            parte_imaginaria = float(input("Digita la parte imaginaria del complejo: "))

            complejo = complex(parte_real, parte_imaginaria)

            dibujar_complejos(complejo)

        elif opcion == 10:
            print("Gracias por usar el programa de numeros complejos :D")
            seguir_programa = "N"
else:
    print("Gracias. Vuelva pronto")
    s.exit()
