from flask import Flask, render_template, request

from Complejos.formas_complejos.binomica import forma_binomica

app = Flask(__name__)


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/complejos', methods=['POST', 'GET'])
def binomica():
    if request.method == 'POST':
        parte_real = request.form['parteReal']
        parte_imaginaria = request.form['parteImaginaria']
        complejo_binomica = forma_binomica(float(parte_real), float(parte_imaginaria))
        operacion = request.form['operacion']
        if operacion == 'binomica':
            print(operacion)

        return render_template('complejos_con_grafico.html', complejo=complejo_binomica)
    else:
        return render_template('complejos_con_grafico.html')


if __name__ == '__main__':
    app.run(port=8080)
