from flask import Flask, render_template

# Creamos la interface de Flask 

app = Flask(__name__)

# Creamos un decorador para la ruta

@app.route("/")
def index():
    return render_template(index.html)