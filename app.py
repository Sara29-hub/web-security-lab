from flask import render_template
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

@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

if __name__ == "__main__":
    app.run(debug=True)
