from flask import Flask, make_response, request, json, jsonify
from models import Usuario
#from settings import Session
from settings import session as db_session #He quitado el session de arriba para ponerlo aqui commo otro nombre para la linea de usuario_db ya que si no habria dos session el de flask y el de settings
from flask import session as flask_session
from flask import redirect
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

    #he cambiado session.query por db_session.query, ya que iba a haber dos session en esta parte del codigo, el de flask y el de settings, asi que he tenido que 
    # renombrar el nombre de session en el import
    usuario_db = db_session.query(Usuario).filter_by(Email = email_ingresado).first()

    
    if not usuario_db or not usuario_db.autenticar(contraseña_ingresada):
        return make_response(jsonify({"Mensaje": "Credenciales invalidas "}), 401)

    flask_session["usuario"] = usuario_db.Email #Revisar esta linea para estudiar esto 
    flask_session["user_id"] = usuario_db.id
    flask_session["rol"] = usuario_db.Rol
    return make_response(jsonify({"Mensaje": "Usuario conectado"}), 200)
    
    

@app.route("/logout")
def logout():
    flask_session.clear()
    return redirect("/")


    
    