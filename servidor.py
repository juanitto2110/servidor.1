from flask import Flask, jsonify, request# Importa Flask para crear el servidor y jsonify para formatear las respuestas como JSON

app = Flask(_name_)

# Base de datos simulada
base_datos = {
    "usuarios": [
        {"id": 1, "nombre": "Juan"},
        {"id": 2, "nombre": "Maria"},
        {"id": 3, "nombre": "manuel"},
        {"id": 4, "nombre": "Alexa"},
        {"id": 5, "nombre": "Kevin"},
        {"id": 6, "nombre": "Dario"},
        {"id": 7, "nombre": "Andres"},
        {"id": 8, "nombre": "Stivel"}
      ]
}
# Ruta para obtener los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(base_datos["usuarios"])  # Devuelve la lista de usuarios en formato JSON

# Método POST para agregar nuevos usuarios 
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    nuevo_usuario = request.get_json()  # Obtiene los datos enviados en la solicitud POST
    if not nuevo_usuario or not "nombre" in nuevo_usuario:  # Valida que el nombre este presente
        return jsonify({"error": "El nombre es requerido"}), 400
    # Validaciones adicionales
    nombre = nuevo_usuario["nombre"]
    
    # Verifica que el nombre no esté vacío y tenga al menos 3 caracteres
    if len(nombre.strip()) == 0:
        return jsonify({"error": "El nombre no puede estar vacío"}), 400
    elif len(nombre) < 3:
        return jsonify({"error": "El nombre debe tener al menos 3 caracteres"}), 400

    # Asignacion automatica de un nuevo ID
    nuevo_usuario["id"] = len(base_datos["usuarios"]) + 1
    base_datos["usuarios"].append(nuevo_usuario)  # Agrega el nuevo usuario a la base de datos simulada

    return jsonify(nuevo_usuario), 201  # Responde con el nuevo usuario creado y el codigo 201 (Created)

if _name_ == '_main_':
    app.run(port=5000)  # Ejecuta el servidor en el puerto 5000
