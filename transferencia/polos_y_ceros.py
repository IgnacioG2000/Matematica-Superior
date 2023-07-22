from scipy import signal


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