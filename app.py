from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import re
from datetime import datetime

app = Flask(__name__)
CORS(app)

usuarios = []
# Funciones de validación


def validar_nombre(nombre):
    return nombre.strip() != ""
    
    
def validar_email(email):
    return re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email)

def validar_telefono(telefono):
    return re.match(r'^\+\d{1,3}\s?\d{6,14}$', telefono)

@app.route('/registrar', methods=['POST'])
def registrar_usuario():
    datos = request.json
    nombre = datos.get("nombre", "").strip()
    email = datos.get("email", "").strip()
    telefono = datos.get("telefono", "").strip()

    if not validar_nombre(nombre):
        return jsonify({"error": "El nombre no puede estar vacío."}), 400
    if not validar_email(email):
        return jsonify({"error": "El correo electrónico no es válido."}), 400
    if not validar_telefono(telefono):
        return jsonify({"error": "El número de teléfono no es válido. Debe tener prefijo + y solo dígitos."}), 400

    nuevo_usuario = {
        "nombre": nombre,
        "email": email,
        "telefono": telefono,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
 #   Verificar si el usuario ya existe
    usuarios.append(nuevo_usuario)
    return jsonify({"mensaje": "Usuario registrado con éxito."}), 200

# Obtener todos los usuarios registrados
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios), 200

@app.route('/borrar-todo', methods=['DELETE'])
def borrar_usuarios():
    usuarios.clear()
    return jsonify({"mensaje": "Todos los registros han sido eliminados."}), 200

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

if __name__ == '__main__':
    app.run(debug=True)
