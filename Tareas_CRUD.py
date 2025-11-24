from flask import Flask, request, jsonify, make_response
from models import Tarea, Usuario
from settings import session
app = Flask(__name__)



@app.route("/create", methods = "POST")
def crear():
    try:

        if not request.is_json:
            return make_response(jsonify({"Mensaje": "El contenido debe ser JSON"}), 400)
        
        data = request.json

        tarea = Tarea(

            Nombre_tarea = data["Nombre_tarea"],
            Creado_tarea = data["Creado_tarea"],
            Actualizado_tarea = data["Actualizado_tarea"],
            Contenido_tarea = data["Contenido_tarea"]

        )

        session.add(tarea)
        session.commit()

        return make_response(jsonify({"Mensaje": "Tarea creada"}), 201)

    except Exception as e:
        print("Error al introducir la tarea", e)
        session.rollback()
        return make_response(jsonify({"Mensaje": "Error al crear la tarea "}), 500)






@app.route("/read", methods = "GET")
def obtener():
     try:
        Tareas = session.query(Tarea).all()

        return make_response(jsonify([Usuario.json() for Usuario in Tareas]), 200)
     except Exception as e:
        return make_response(jsonify({'Mensaje': 'Error al obtener las tareas'}), 500)







@app.route("/update", methods = "PUT")
def actualizar():
    try:
        data = request.get_json()
        ID_tarea = data.get("id")

        tarea = session.query(Tarea).filter_by(id = ID_tarea).first()

        if not tarea:
            return make_response(jsonify({"Mensaje": "Tarea no encontrada"}), 404)
        
        Tarea.Contenido = data.get("Nuevo contenido", Tarea.Contenido)
        Tarea.Nombre = data.get("Nuevo nombre", Tarea.Nombre)
        Tarea.Update_at = data.get("Fecha modificacion", Tarea.Update_at)

        session.commit()
        return make_response(jsonify({"Mensaje": "Tarea actualizada"}), 200)

        


    except Exception as e:  
        print("Error al actualizar la tarea", e)
        session.rollback()
        return make_response(jsonify({'Mensaje': 'Error al actualizar la tarea'}), 500)








@app.route("/delete", methods = "DELETE")
def eliminar():
    try:
        Id_tarea = request.get_json().get("id")
        tarea = session.query(Tarea).filter_by(id = Id_tarea).first

        if not tarea:
            return make_response(jsonify({"Mensaje": "No se ha encontrado la tarea"}), 404)
    
        session.delete(tarea)
        session.commit()
    
        return make_response(jsonify({"Mensaje": "Tarea eliminada"}), 200)
    except Exception as e:
        session.rollback()
        print("Error al eliminar la tarea ", e)
        return make_response(jsonify({"Mensaje": "Error al eliminar la tarea "}), 500)
