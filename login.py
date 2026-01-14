from flask import Flask, make_response, request, json, jsonify
from models import Usuario
from settings import Session, session
#from flask_cors import CORS
from app_instance import app

#CORS(app)


@app.route("/login", methods = ["POST"])
def login():
    if not request.is_json:
        return make_response(jsonify({"Mensaje": "El usuario debe ser en formato Json"}), 400)
    
    data = request.get_json()

    email_ingresado = data.get("email")
    contraseña_ingresada = data.get("password")
    
    if not email_ingresado or not contraseña_ingresada:
        return make_response(
            jsonify({"Mensaje": "Email y contraseña son obligatorios"}),
            400
        )

    usuario_db = session.query(Usuario).filter_by(Email = email_ingresado).first()

    
    if not usuario_db or not usuario_db.autenticar(contraseña_ingresada):
        return make_response(jsonify({"Mensaje": "Credenciales invalidas "}), 401)

    return make_response(jsonify({"Mensaje": "Usuario conectado"}), 200)
    
    




    
    