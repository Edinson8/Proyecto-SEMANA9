from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Bienvenidos a mi proyecto"

@app.route('/usuarios/<nombre>')
def usuario(nombre):
    return f'Hola, {nombre}!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa el puerto que Render asigna
    app.run(host="0.0.0.0", port=port, debug=True)

