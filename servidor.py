from flask import Flask, jsonify# Importa Flask para crear el servidor y jsonify para formatear las respuestas como JSON

app = Flask(_name_)

# Base de datos simulada
base_datos = {
    "usuarios": [
        {"id": 1, "nombre": "Juan"},
        {"id": 2, "nombre": "María"}
        {"id": 3, "nombre": "manuel"}
        {"id": 4, "nombre": "Alexa"}
        {"id": 5, "nombre": "Kevin"}
        {"id": 6, "nombre": "Dario"}
        {"id": 7, "nombre": "Andres"}
        {"id": 8, "nombre": "Stivel"}
    ]
}
# Ruta para obtener los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(base_datos["usuarios"]) # Devuelve la lista de usuarios en formato 
JSON
app.run(port=5000)
