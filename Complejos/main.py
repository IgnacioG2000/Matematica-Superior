from Complejos.formas_complejos.binomica import forma_binomica
from Complejos.formas_complejos.polar import *
from Complejos.grafico import dibujar_complejos
from Complejos.operaciones import *
from menu import menu

menu()
opcion = int(input("\nIngresa la opcion deseada: "))

if opcion == 1:
    parte_real = float(input("\nDigita la parte real del complejo: "))
    parte_imaginaria = float(input("Digita la parte imaginaria del complejo: "))

    binomica = forma_binomica(parte_real, parte_imaginaria)
    print(f"Forma binomica: {binomica}")

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
    print(f"Suma = {suma}")

elif opcion == 4:
    parte_real_1 = float(input("\nDigita la parte real del complejo 1: "))
    parte_imaginaria_1 = float(input("Digita la parte imaginaria del complejo 1: "))
    parte_real_2 = float(input("Digita la parte real del complejo 2: "))
    parte_imaginaria_2 = float(input("Digita la parte imaginaria del complejo 2: "))

    resta = resta(parte_real_1, parte_imaginaria_1, parte_real_2, parte_imaginaria_2)
    print(f"Suma = {resta}")

elif opcion == 5:
    parte_real_1 = float(input("\nDigita la parte real del complejo 1: "))
    parte_imaginaria_1 = float(input("Digita la parte imaginaria del complejo 1: "))
    parte_real_2 = float(input("Digita la parte real del complejo 2: "))
    parte_imaginaria_2 = float(input("Digita la parte imaginaria del complejo 2: "))

    producto = multiplicacion(parte_real_1, parte_imaginaria_1, parte_real_2, parte_imaginaria_2)
    print(f"Producto = {producto}")

elif opcion == 6:
    parte_real_1 = float(input("\nDigita la parte real del complejo 1: "))
    parte_imaginaria_1 = float(input("Digita la parte imaginaria del complejo 1: "))
    parte_real_2 = float(input("Digita la parte real del complejo 2: "))
    parte_imaginaria_2 = float(input("Digita la parte imaginaria del complejo 2: "))

    cociente = division(parte_real_1, parte_imaginaria_1, parte_real_2, parte_imaginaria_2)
    print(f"Producto = {cociente}")


elif opcion == 7:
    parte_real = float(input("\nDigita la parte real del complejo: "))
    parte_imaginaria = float(input("Digita la parte imaginaria del complejo: "))
    exponente = float(input("Digita el exponente: "))

    resultado = potencia(parte_real, parte_imaginaria, exponente)
    print(f"Resultado = {resultado}")

if opcion == 8:
    parte_real = float(input("\nDigita la parte real del complejo: "))
    parte_imaginaria = float(input("Digita la parte imaginaria del complejo: "))

    complejo = complex(parte_real, parte_imaginaria)

    dibujar_complejos(complejo)
