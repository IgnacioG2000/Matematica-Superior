from flask import Flask, render_template, request

from Complejos.formas_complejos.binomica import forma_binomica
from Complejos.formas_complejos.exponencial import forma_exponencial
from Complejos.formas_complejos.polar import forma_polar
from Complejos.formas_complejos.trigonometrica import forma_trigonometrica

app = Flask(__name__)


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/complejos', methods=['POST', 'GET'])
def complejos_con_grafico():
    if request.method == 'POST':
        parte_real = request.form['parteReal']
        parte_imaginaria = request.form['parteImaginaria']
        operacion = request.form['operacion']
        if operacion == 'binomica':
            complejo_binomica = forma_binomica(float(parte_real), float(parte_imaginaria))
            return render_template('complejos_con_grafico.html', complejo=complejo_binomica, operacion=operacion)
        elif operacion == 'exponencial':
            complejo_exponencial = forma_exponencial(float(parte_real), float(parte_imaginaria))
            return render_template('complejos_con_grafico.html', complejo=complejo_exponencial, operacion=operacion)
        elif operacion == 'trigonometrica':
            complejo_trigonometrica = forma_trigonometrica(float(parte_real), float(parte_imaginaria))
            return render_template('complejos_con_grafico.html', complejo=complejo_trigonometrica, operacion=operacion)
        else:
            complejo_polar = forma_polar(float(parte_real), float(parte_imaginaria))
            return render_template('complejos_con_grafico.html', complejo=complejo_polar, operacion=operacion)
    else:
        return render_template('complejos_con_grafico.html')


if __name__ == '__main__':
    app.run(port=8080)
