from scipy import signal
import matplotlib.pyplot as plt
import io
import base64


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
