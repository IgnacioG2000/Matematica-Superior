from flask import Flask, render_template, request

from Complejos.calculos.operaciones import potencia, raiz_cuadrada, bhaskara, logaritmo_natural_complejo, \
    suma_funciones_por_fasores
from funciones_auxiliares import mostrar_complejo_segun_opcion, realizar_operacion_segun_operador
from laplace.operaciones import L, armar_ecuacion, L_diff, resolver_ecuacion, inv_L
from sympy.abc import t,s
from sympy import Function

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

        # TODO: hacer el hidden como en dds -> si el tipo de senial 1 y 2 son diferentes, que se muestre este select
        opcion_muestra = request.form['tipoFuncionSuma']

        resultado = suma_funciones_por_fasores(modulo1, fase1, tipo_senial1, modulo2, fase2, tipo_senial2, frecuencia,
                                               opcion_muestra)

        return render_template('suma_fasores.html', resultado=resultado)
    else:
        return render_template('suma_fasores.html')


@app.route('/teoriaLaplace', methods=['GET'])
def teoria_laplace():
    return render_template('teoria_laplace.html')


@app.route('/transf_laplace', methods=['GET', 'POST'])
def transformada_laplace():
    if request.method == 'POST':
        transformada = str(request.form['transformada'])

        resultado = L(transformada)

        return render_template('transformada_laplace.html', resultado=resultado)

    else:
        return render_template('transformada_laplace.html')


@app.route('/ec_diferencial_laplace', methods=['GET', 'POST'])
def ec_dif_laplace():
    if request.method == 'POST':
        variable = str(request.form['tipoVariable'])
        coef_deriv_segunda = int(request.form['coefDerivadaSegunda'])
        coef_deriv_primera = int(request.form['coefDerivadaPrimera'])
        coef_funcion = int(request.form['coefFuncion'])
        term_indep = (request.form['terminoIndependiente'])
        print(type(term_indep))
        f0 = int(request.form['f0'])
        print(type(f0))
        fp0 = int(request.form['fp0'])


        ec = armar_ecuacion(coef_deriv_segunda * L_diff(variable, f0, fp0, 0, 2) +
                            coef_deriv_primera * L_diff(variable, f0, 0) +
                            coef_funcion * L_diff(variable, 0, 0, 0, 0),
                            L(term_indep))

        print(ec)
        variable = Function(variable.upper())(s)
        solucion_en_laplace = resolver_ecuacion(ec, variable)
        print(solucion_en_laplace)

        solucion = inv_L(solucion_en_laplace[variable], t)

        variable = Function(variable)(t)

        return render_template('ec_diferenciales_laplace.html', solucion=solucion, variable=variable)

    else:
        return render_template('ec_diferenciales_laplace.html')


if __name__ == '__main__':
    app.run(port=8080)
