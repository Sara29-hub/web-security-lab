from flask import Flask, make_response, request, json, jsonify
from models import Usuario

from settings import session as db_session 
from flask import session as flask_session
from flask import redirect

from app_instance import app





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

    
    usuario_db = db_session.query(Usuario).filter_by(Email = email_ingresado).first()

    
    if not usuario_db or not usuario_db.autenticar(contraseña_ingresada):
        return make_response(jsonify({"Mensaje": "Credenciales invalidas "}), 401)

    flask_session["usuario"] = usuario_db.Email 
    flask_session["user_id"] = usuario_db.id
    flask_session["rol"] = usuario_db.Rol
    return make_response(jsonify({"Mensaje": "Usuario conectado"}), 200)
    
    

@app.route("/logout")
def logout():
    flask_session.clear()
    return redirect("/")


    
    
