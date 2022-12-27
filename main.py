from flask import Flask, render_template, request

from Complejos.calculos.operaciones import potencia,raiz_cuadrada, bhaskara, logaritmo_natural_complejo, suma_funciones_por_fasores
from funciones_auxiliares import mostrar_complejo_segun_opcion, realizar_operacion_segun_operador

app = Flask(__name__)


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/complejos', methods=['POST', 'GET'])
def complejos_con_grafico():
    if request.method == 'POST':
        parte_real = float(request.form['parteReal'])
        parte_imaginaria = float(request.form['parteImaginaria'])
        opcion = request.form['visualizacion']

        return mostrar_complejo_segun_opcion(parte_real, parte_imaginaria, opcion, 'complejos_con_grafico.html')

    else:
        return render_template('complejos_con_grafico.html')


@app.route('/complejos_operaciones', methods=['GET', 'POST'])
def operaciones_complejos():
    if request.method == 'POST':
        complejo1 = complex(request.form['complejoOperaciones1'])
        complejo2 = complex(request.form['complejoOperaciones2'])
        operacion = request.form['operacion']

        return realizar_operacion_segun_operador(complejo1, complejo2, operacion, 'operaciones_con_complejos.html')

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
