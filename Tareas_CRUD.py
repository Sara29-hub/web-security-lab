from flask import Flask, request, jsonify, make_response
from models import Tarea, Usuario
from settings import session
from app_instance import app

print(">>> CARGANDO Tareas_CRUD")

@app.route("/tareas/create", methods = ["POST"])
def crear():
    try:

        if not request.is_json:
            return make_response(jsonify({"Mensaje": "El contenido debe ser JSON"}), 400)
        
        data = request.json

        tarea = Tarea(

            Nombre = data["Nombre"],
            Contenido = data["Contenido"]

        )

        session.add(tarea)
        session.commit()

        return make_response(jsonify({"Mensaje": "Tarea creada"}), 201)

    except Exception as e:
        print("Error al introducir la tarea", e)
        session.rollback()
        return make_response(jsonify({"Mensaje": "Error al crear la tarea "}), 500)






@app.route("/tareas/read", methods = ["GET"])
def obtener():
     try:
        Tareas = session.query(Tarea).all()

        return make_response(jsonify([Tarea.json() for Tarea in Tareas]), 200)
     except Exception as e:
        return make_response(jsonify({'Mensaje': 'Error al obtener las tareas'}), 500)







@app.route("/tareas/update", methods = ["PUT"])
def actualizar():
    try:
        data = request.get_json()
        ID_tarea = data.get("id")

        tarea = session.query(Tarea).filter_by(id = ID_tarea).first()

        if not tarea:
            return make_response(jsonify({"Mensaje": "Tarea no encontrada"}), 404)
        
        tarea.Contenido = data.get("Nuevo contenido", tarea.Contenido)
        tarea.Nombre = data.get("Nuevo nombre", tarea.Nombre)
        

        session.commit()
        return make_response(jsonify({"Mensaje": "Tarea actualizada"}), 200)

        


    except Exception as e:  
        print("Error al actualizar la tarea", e)
        session.rollback()
        return make_response(jsonify({'Mensaje': 'Error al actualizar la tarea'}), 500)








@app.route("/tareas/delete", methods = ["DELETE"])
def eliminar():
    try:
        Id_tarea = request.get_json().get("id")
        tarea = session.query(Tarea).filter_by(id = Id_tarea).first()

        if not tarea:
            return make_response(jsonify({"Mensaje": "No se ha encontrado la tarea"}), 404)
    
        session.delete(tarea)
        session.commit()
    
        return make_response(jsonify({"Mensaje": "Tarea eliminada"}), 200)
    except Exception as e:
        session.rollback()
        print("Error al eliminar la tarea ", e)
        return make_response(jsonify({"Mensaje": "Error al eliminar la tarea "}), 500)
