from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/binomica', methods=['POST'])
def binomica():
    if request.method == 'POST':
        parte_real = request.form['parte_real']
        parte_imaginaria = request.form['parte_imaginaria']
        print(parte_real)
        print(parte_imaginaria)
        return "recibido"


if __name__ == '__main__':
    app.run(port=8080)
