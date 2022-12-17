from flask import Flask, render_template, request

from Complejos.formas_complejos.binomica import forma_binomica

app = Flask(__name__)


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/binomica', methods=['POST', 'GET'])
def binomica():
    if request.method == 'POST':
        parte_real = request.form['parteReal']
        parte_imaginaria = request.form['parteImaginaria']
        complejo_binomica = forma_binomica(float(parte_real), float(parte_imaginaria))

        return render_template('complejos_binomica.html', complejo=complejo_binomica)
    else:
        return render_template('complejos_binomica.html')


if __name__ == '__main__':
    app.run(port=8080)
