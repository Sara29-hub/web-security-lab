from flask import Flask, render_template, request, redirect, jsonify, make_response, json
from models import Usuario, Tarea
from settings import Session, session
from decorators import admin_required, login_required
#from flask_limiter import Limiter
from app_instance import app




@app.route("/Usuario/create", methods= ["POST"])
#@limiter.limit("5 per minute")
def Crear():

    
        try:    

            if not request.is_json:
                return make_response(jsonify({"Mensaje": "El contenido debe ser JSON"}), 400)

            data = request.get_json()

            usuario =  Usuario(

                Nombre = data["Nombre usuario"],
                Apellidos = data["Apellidos usuario"],
                Email = data["Email usuario"],
                Rol = "usuario"
                
                )
            usuario.contraseña = data["password"]


            session.add(usuario)
            session.commit()
            
            return make_response(jsonify({"Mensaje": "Usuario creado"}), 201)
        
        except Exception as e:
            print("Error al introducir el usuario ", e)
            session.rollback()
            return make_response(jsonify({"Mensaje": "Error al crear el usuario "}), 500)



    

@app.route("/Usuario/read", methods= ["GET"])
@admin_required
def Obtener():

    try:
        Usuarios = session.query(Usuario).all() 

        return make_response(jsonify([u.json() for u in Usuarios]), 200)
    except Exception as e:
        return make_response(jsonify({'Mensaje': 'Error al obtener los usuarios'}), 500)

        
    

@app.route("/Usuario/update", methods= ["PUT"])
@login_required
def Actualizar():
    try:

        data = request.get_json()
        ID_usuario = data.get("id")


        User = session.query(Usuario).filter_by(id = ID_usuario).first()

        
        if not User:
            return make_response(jsonify({"Mensaje": "Usuario no encontrado"}), 404)


        User.Nombre = data.get("Nuevo nombre", User.Nombre)
        User.Apellidos = data.get("Nuevo apellido", User.Apellidos)
        User.Email = data.get("Nuevo email", User.Email)
        User.Rol = data.get("Nuevo rol", User.Rol)  
        if "Nueva contraseña" in data:
         User.contraseña = data["Nueva contraseña"]


        session.commit()
        return make_response(jsonify({"Mensaje": "Usuario actualizado "}), 200)
        
    except Exception as e:
        print("Error al actualizar", e)
        session.rollback()
        return make_response(jsonify({'Mensaje': 'Error al actualizar el usuario'}), 500)
    



@app.route("/Usuario/delete", methods= ["DELETE"])
@login_required
def Eliminar():
    try:
        data = request.get_json() 
    
        if not data or "id" not in data:
            return make_response(jsonify({"Mensaje": "No se permite campos vacios"}))
        
        ID_usuario = data['id']
        User = session.query(Usuario).filter_by(id = ID_usuario).first()

        if not User:
            return make_response(jsonify({"Mensaje": "Usuario no encontrado"}), 404)
    
        
        session.delete(User)
        session.commit()

        return make_response(jsonify({"Mensaje": "Usuario eliminado "}), 200)
    
    except Exception as e:
        session.rollback()
        print("Error al eliminar el usuario ", e)
        return make_response(jsonify({"Mensaje": "Error al eliminar el usuario "}), 500)
