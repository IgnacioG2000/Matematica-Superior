from flask import Flask, render_template, request

from Complejos.calculos.operaciones import suma_complejos, resta_complejos, multiplicacion, division, potencia, \
    raiz_cuadrada, bhaskara, logaritmo_natural_complejo, suma_funciones_por_fasores
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
        complejo1 = complex(request.form['complejoOperaciones1'])
        complejo2 = complex(request.form['complejoOperaciones2'])
        operacion = request.form['operacion']
        if operacion == 'suma':
            complejo_suma = suma_complejos(complejo1, complejo2)
            return render_template('operaciones_con_complejos.html', complejo=complejo_suma, operacion=operacion)
        elif operacion == 'resta':
            complejo_resta = resta_complejos(complejo1, complejo2)
            return render_template('complejos_con_grafico.html', complejo=complejo_resta, operacion=operacion)
        elif operacion == 'multiplicacion':
            complejo_multiplicacion = multiplicacion(complejo1, complejo2)
            return render_template('complejos_con_grafico.html', complejo=complejo_multiplicacion, operacion=operacion)
        else:
            complejo_cociente = division(complejo1, complejo2)
            return render_template('complejos_con_grafico.html', complejo=complejo_cociente, operacion=operacion)

    else:
        return render_template('operaciones_con_complejos.html')


@app.route('/complejos_exponente', methods=['GET', 'POST'])
def exponencial():
    if request.method == 'POST':
        complejo = complex(request.form['complejoExp'])
        exponente = float(request.form['exponente'])
        resultado = potencia(complejo, exponente)
        return render_template('potenciacion_complejos.html', resultado=resultado)
    else:
        return render_template('potenciacion_complejos.html')


@app.route('/complejos_raiz', methods=['GET', 'POST'])
def raiz_cuadrada_complejo():
    if request.method == 'POST':
        complejo = complex(request.form['complejoRaiz'])

        resultado1, resultado2 = raiz_cuadrada(complejo)

        return render_template('raiz_cuadrada.html', resultado1=resultado1, resultado2=resultado2)
    else:
        return render_template('raiz_cuadrada.html')


@app.route('/cuadratica_complejos', methods=['GET', 'POST'])
def resolvente():
    if request.method == 'POST':
        complejo1 = complex(request.form['complejo1'])
        complejo2 = complex(request.form['complejo2'])
        complejo3 = complex(request.form['complejo3'])

        resultado1, resultado2 = bhaskara(complejo1, complejo2, complejo3)

        return render_template('ecuacion_compleja.html', resultado1=resultado1, resultado2=resultado2)
    else:
        return render_template('ecuacion_compleja.html')


@app.route('/complejos_logaritmo', methods=['GET', 'POST'])
def logaritmo_natural():
    if request.method == 'POST':
        complejo = complex(request.form['logNatural'])

        resultado = logaritmo_natural_complejo(complejo)
        return render_template('logaritmo_natural.html', resultado=resultado)
    else:
        return render_template('logaritmo_natural.html')


@app.route('/fasores', methods=['GET', 'POST'])
def fasores():
    if request.method == 'POST':
        modulo1 = float(request.form['amplitud1'])
        fase1 = float(request.form['fase1'])
        tipo_senial1 = request.form['tipoFuncion1']

        modulo2 = float(request.form['amplitud2'])
        fase2 = float(request.form['fase2'])
        tipo_senial2 = request.form['tipoFuncion2']

        frecuencia = request.form['frecuencia']

        resultado = suma_funciones_por_fasores(modulo1, fase1, tipo_senial1, modulo2, fase2, tipo_senial2, frecuencia)

        return render_template('suma_fasores.html', resultado=resultado)
    else:
        return render_template('suma_fasores.html')


if __name__ == '__main__':
    app.run(port=8080)
