from flask import render_template
from Concessionaria import app

@app.route('/')
def homepage():  # put application's code here
    return render_template('index.html')

@app.route('/index.html')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/form.html')
def cadastro():  # put application's code here
    return render_template('form.html')

@app.route('/veiculo.html')
def veiculo():  # put application's code here
    return render_template('veiculo.html')

@app.route('/end.html')
def end():  # put application's code here
    return render_template('end.html')

@app.route('/registro.html')
def registro():  # put application's code here
    return render_template('registro.html')