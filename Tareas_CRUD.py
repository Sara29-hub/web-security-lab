from flask import Flask, request, jsonify, make_response
from flask import session as flask_session
from models import Tarea, Usuario
from datetime import datetime
from settings import session as db_session
from app_instance import app

print(">>> CARGANDO Tareas_CRUD")

@app.route("/tareas/create", methods = ["POST"])
def crear():
    try:

        user_id = flask_session.get("user_id")
        if not user_id:
            return make_response(jsonify({"Mensaje": "No autenticado"}), 401)

        if not request.is_json:
            return make_response(jsonify({"Mensaje": "El contenido debe ser JSON"}), 400)
        
        
        data = request.json

        if "Fecha" not in data:
            return make_response(jsonify({"Mensaje": "Falta el campo Fecha"}), 400)

        fecha = datetime.strptime(data["Fecha"], "%Y-%m-%d").date()

        tarea = Tarea(

            Nombre = data["Nombre"],
            Contenido = data["Contenido"],
            Fecha=fecha,
            usuario_id = flask_session['user_id']

        )

        db_session.add(tarea)
        db_session.commit()

        return make_response(jsonify({"Mensaje": "Tarea creada"}), 201)

    except Exception as e:
        print("Error al introducir la tarea", e)
        db_session.rollback()
        return make_response(jsonify({"Mensaje": "Error al crear la tarea "}), 500)






@app.route("/tareas/read", methods = ["GET"])
def obtener():
     try:
        #Tareas = session.query(Tarea).all()

        user_id = flask_session.get("user_id")
        if not user_id:
            return make_response(jsonify({"Mensaje": "No autenticado"}), 401)

        if flask_session["rol"] == "admin":
            Tareas = db_session.query(Tarea).all()
        else:

            Tareas = db_session.query(Tarea).filter_by(usuario_id=flask_session['user_id']).all()

        

        return make_response(jsonify([Tarea.json() for Tarea in Tareas]), 200)
     except Exception as e:
        return make_response(jsonify({'Mensaje': 'Error al obtener las tareas'}), 500)







@app.route("/tareas/update", methods = ["PUT"])
def actualizar():
    try:
        data = request.get_json()

        if not data:
            return make_response(jsonify({"Mensaje": "No se han enviado datos"}), 400)

        ID_tarea = data.get("id")

        if not ID_tarea:
            return make_response(jsonify({"Mensaje": "Falta el id"}), 400)

        #Nueva comprobacion de ataque IDOR
        user_id = flask_session.get("user_id")
        if not user_id:
            return make_response(jsonify({"Mensaje": "No autenticado"}), 401)


        tarea = db_session.query(Tarea).filter_by(id = ID_tarea, usuario_id=user_id).first()


        if not tarea:
            return make_response(jsonify({"Mensaje": "Tarea no encontrada"}), 404)
        
        tarea.Contenido = data.get("Contenido", tarea.Contenido)
        tarea.Nombre = data.get("Nombre", tarea.Nombre)

        
        if "Fecha" in data and data["Fecha"]:
            tarea.Fecha = datetime.strptime(data["Fecha"], "%Y-%m-%d").date()

        

        db_session.commit()
        db_session.refresh(tarea)
        return make_response(jsonify({"Mensaje": "Tarea actualizada"}), 200)


    except Exception as e:  
        print("Error al actualizar la tarea", e)
        db_session.rollback()
        return make_response(jsonify({'Mensaje': 'Error al actualizar la tarea'}), 500)








@app.route("/tareas/delete", methods = ["DELETE"])
def eliminar():
    try:
        Id_tarea = request.get_json().get("id")

        
        user_id = flask_session.get("user_id")
        if not user_id:
            return make_response(jsonify({"Mensaje": "No autenticado"}), 401)
    


        tarea = db_session.query(Tarea).filter_by(id = Id_tarea, usuario_id=user_id).first()

        

        if not tarea:
            return make_response(jsonify({"Mensaje": "No se ha encontrado la tarea"}), 404)
        
        #Nueva comprobacion de ataque IDOR
      
        db_session.delete(tarea)
        db_session.commit()
    
        return make_response(jsonify({"Mensaje": "Tarea eliminada"}), 200)
    except Exception as e:
        db_session.rollback()
        print("Error al eliminar la tarea ", e)
        return make_response(jsonify({"Mensaje": "Error al eliminar la tarea "}), 500)
