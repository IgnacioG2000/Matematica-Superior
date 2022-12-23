from flask import Flask, render_template, request

from Complejos.calculos.operaciones import suma_complejos, resta_complejos, multiplicacion, division, potencia, \
    raiz_cuadrada, bhaskara
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
        parte_real = float(request.form['parteReal'])
        parte_imaginaria = float(request.form['parteImaginaria'])
        operacion = request.form['visualizacion']
        if operacion == 'binomica':
            complejo_binomica = forma_binomica(parte_real, parte_imaginaria)
            return render_template('complejos_con_grafico.html', complejo=complejo_binomica, operacion=operacion)
        elif operacion == 'exponencial':
            complejo_exponencial = forma_exponencial(parte_real, parte_imaginaria)
            return render_template('complejos_con_grafico.html', complejo=complejo_exponencial, operacion=operacion)
        elif operacion == 'trigonometrica':
            complejo_trigonometrica = forma_trigonometrica(parte_real, parte_imaginaria)
            return render_template('complejos_con_grafico.html', complejo=complejo_trigonometrica, operacion=operacion)
        else:
            complejo_polar = forma_polar(parte_real, parte_imaginaria)
            return render_template('complejos_con_grafico.html', complejo=complejo_polar, operacion=operacion)
    else:
        return render_template('complejos_con_grafico.html')


@app.route('/complejos_operaciones', methods=['GET', 'POST'])
def operaciones_complejos():
    if request.method == 'POST':
        parte_real1 = float(request.form['parteReal1'])
        parte_imaginaria1 = float(request.form['parteImaginaria1'])
        parte_real2 = float(request.form['parteReal2'])
        parte_imaginaria2 = float(request.form['parteImaginaria2'])
        operacion = request.form['operacion']
        if operacion == 'suma':
            complejo_suma = suma_complejos(parte_real1, parte_imaginaria1, parte_real2, parte_imaginaria2)
            return render_template('operaciones_con_complejos.html', complejo=complejo_suma, operacion=operacion)
        elif operacion == 'resta':
            complejo_resta = resta_complejos(parte_real1, parte_imaginaria1, parte_real2, parte_imaginaria2)
            return render_template('complejos_con_grafico.html', complejo=complejo_resta, operacion=operacion)
        elif operacion == 'multiplicacion':
            complejo_multiplicacion = multiplicacion(parte_real1, parte_imaginaria1, parte_real2, parte_imaginaria2)
            return render_template('complejos_con_grafico.html', complejo=complejo_multiplicacion, operacion=operacion)
        else:
            complejo_cociente = division(parte_real1, parte_imaginaria1, parte_real2, parte_imaginaria2)
            return render_template('complejos_con_grafico.html', complejo=complejo_cociente, operacion=operacion)

    else:
        return render_template('operaciones_con_complejos.html')


@app.route('/complejos_exponente', methods=['GET', 'POST'])
def exponencial():
    if request.method == 'POST':
        parte_real = float(request.form['parteReal'])
        parte_imaginaria = float(request.form['parteImaginaria'])
        exponente = float(request.form['exponente'])
        resultado = potencia(parte_real, parte_imaginaria, exponente)
        return render_template('potenciacion_complejos.html', resultado=resultado)
    else:
        return render_template('potenciacion_complejos.html')


@app.route('/complejos_raiz', methods=['GET', 'POST'])
def raiz_cuadrada_complejo():
    if request.method == 'POST':
        parte_real = float(request.form['parteReal'])
        parte_imaginaria = float(request.form['parteImaginaria'])

        resultado1, resultado2 = raiz_cuadrada(parte_real, parte_imaginaria)
        print(resultado1)
        print(resultado2)
        return render_template('raiz_cuadrada.html', resultado1=resultado1, resultado2=resultado2)
    else:
        return render_template('raiz_cuadrada.html')


@app.route('/cuadratica_complejos', methods=['GET', 'POST'])
def resolvente():
    if request.method == 'POST':
        parte_real1 = float(request.form['parteReal1'])
        parte_imaginaria1 = float(request.form['parteImaginaria1'])
        parte_real2 = float(request.form['parteReal2'])
        parte_imaginaria2 = float(request.form['parteImaginaria2'])
        parte_real3 = float(request.form['parteReal3'])
        parte_imaginaria3 = float(request.form['parteImaginaria3'])

        complejo1 = complex(parte_real1, parte_imaginaria1)
        complejo2 = complex(parte_real2, parte_imaginaria2)
        complejo3 = complex(parte_real3, parte_imaginaria3)
        print(complejo1)
        print(complejo2)
        print(complejo3)

        resultado1, resultado2 = bhaskara(complejo1, complejo2, complejo3)
        print(resultado1)
        print(resultado2)
        return render_template('ecuacion_compleja.html', resultado1=resultado1, resultado2=resultado2)
    else:
        return render_template('ecuacion_compleja.html')


if __name__ == '__main__':
    app.run(port=8080)
