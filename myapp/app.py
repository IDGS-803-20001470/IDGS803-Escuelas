import flask
from flask import Blueprint
from flask import Flask, redirect, render_template

from Alumnos.routes import alumnos
from Directivos.routes import directivos
from Maestros.routes import maestros
from flask_wtf.csrf import CSRFProtect

app= flask.Flask(__name__)
app.config['DEBUG']=True
csrf= CSRFProtect()

@app.route('/', methods=['GET', 'POST'])
def home():
    
    return render_template('index.html')


app.register_blueprint(alumnos)

app.register_blueprint(directivos)

app.register_blueprint(maestros)

if __name__=='__main__':
    #csrf.init_app(app)
    app.run()