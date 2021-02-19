import os
from flask import Flask,render_template,request
from werkzeug.utils import secure_filename

app = Flask(__name__)#name almacena el nombre del modulo en el que nos encontramos

app.config['UPLOAD_FOLDER'] = './archivos'

@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/resultado", methods=['GET', 'POST'])
def resultado():
    if request.method == 'POST':
        opcion = int(request.form['opcion'])
        combinaciones = int(request.form['combinaciones'])
        matriz = request.files['matriz']
        filename = "matriz.csv"
        matriz.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if opcion == 1:
            from montecarlo import calcularGanador
            array = calcularGanador(combinaciones)
        if opcion == 2:
            from vecino import calcularGanador
            array = calcularGanador(combinaciones)
    return render_template("resultado.html", array=array)

if __name__ == '__main__':
    app.run()