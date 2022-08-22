import matplotlib.pyplot as plt


def dibujar_complejos(complejo):
    fig, ax = plt.subplots()
    ax.quiver(0, 0, complejo.real, complejo.imag, angles='xy', scale_units='xy', scale=1)
    ax.axis([-1, 4, -6, 1])
    ax.set_xlabel('Parte Real')
    ax.set_ylabel('Parte Imaginaria')
    plt.show()
