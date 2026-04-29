from flask import render_template, session, redirect
from app_instance import app
import User_CRUD
import Tareas_CRUD
import login

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/logout")
def logout_ruta(): 
    return login.logout()

@app.route("/tasks")
def tasks():
    if "usuario" not in session:
        return redirect("/")
    return render_template("tasks.html")

@app.route("/Calendario")
def calendario():
    if "usuario" not in session:
        return redirect("/")
    return render_template("calendario.html")

if __name__ == "__main__":
    app.run(debug=True)
