from scipy import signal
import matplotlib.pyplot as plt
import io
import base64
import numpy as np


def obtener_polos_y_ceros(numerador, denominador):
    # Solicitar al usuario ingresar los coeficientes del numerador y denominador de la función de transferencia
    numerador = list(map(int, numerador.split(',')))
    denominador = list(map(int, denominador.split(',')))

    # Crear el objeto de función de transferencia con los coeficientes ingresados
    transfer_function = signal.TransferFunction(numerador, denominador)

    # Obtener los polos y ceros de la función de transferencia
    polos = transfer_function.poles
    ceros = transfer_function.zeros

    return ceros, polos


def verificar_infinito(numerador, denominador):
    # Convertir los valores ingresados a listas de coeficientes
    numerador = np.trim_zeros(numerador, 'f')  # Eliminar los ceros en el extremo derecho del numerador
    denominador = np.trim_zeros(denominador, 'f')  # Eliminar los ceros en el extremo derecho del denominador

    grado_numerador = len(numerador) - 1
    grado_denominador = len(denominador) - 1

    if grado_numerador < grado_denominador:
        return "La función de transferencia presenta un 0 en el infinito."
    else:
        return "La función de transferencia no presenta un 0 en el infinito."

#TODO: GENERAR ABSTRACCION DE FUNCION TRANSFERENCIA
def verificar_estabilidad(numerador, denominador):
    # Crear la función de transferencia con los coeficientes proporcionados
    numerador = list(map(int, numerador.split(',')))
    denominador = list(map(int, denominador.split(',')))
    transfer_function = signal.TransferFunction(numerador, denominador)

    # Obtener los polos de la función de transferencia
    polos = transfer_function.poles

    # Verificar la estabilidad del sistema
    if all(np.real(polos) < 0) or all(np.real(polos) == 0):
        return "El sistema es estable."
    return "El sistema es inestable."


def generar_constelacion_polos_y_ceros(ceros, polos):
    # Generar el gráfico de polos y ceros
    plt.figure()
    plt.scatter(polos.real, polos.imag, marker='x', color='red', label='Polos')
    plt.scatter(ceros.real, ceros.imag, marker='o', color='blue', label='Ceros')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginaria')
    plt.title('Diagrama de Polos y Ceros')
    plt.legend()

    # Convertir el gráfico en una imagen y codificarla en base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    diagrama = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close()

    return diagrama
