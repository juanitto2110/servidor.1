import requests

# Función para obtener usuarios (Método GET)
def obtener_usuarios():
    response = requests.get('http://localhost:5000/usuarios')
    if response.status_code == 200:  # Si la respuesta es exitosa (código 200)
        usuarios = response.json()  # Convierte el cuerpo de la respuesta JSON a un objeto de Python (lista de diccionarios)
        print("Usuarios encontrados:")
        for usuario in usuarios:  # Itera sobre la lista de usuarios y muestra sus datos
            print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}")
    else:
        print("Error al obtener usuarios")  # Muestra un mensaje de error si la solicitud falla

# Función para crear un nuevo usuario (Método POST)
def crear_usuario(nombre):
    nuevo_usuario = {'nombre': nombre}  # Datos del nuevo usuario
    response = requests.post('http://localhost:5000/usuarios', json=nuevo_usuario)
    
    if response.status_code == 201:
