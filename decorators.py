from functools import wraps
from flask import abort, session, redirect, url_for, flash



def admin_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
            
            if 'user_id' not in session:
                  flash("Debes iniciar sesion primero")
                  return redirect(url_for("home"))

            
            if session.get('rol') != 'admin':
                  flash('Acceso denegado: Se requiere permisos de administrador')
                  return redirect(url_for("home"))
            return f(*args, **kwargs)
    return decorated_function


def login_required(f):
      @wraps(f)
      def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                  flash('Acceso denegado: Se requiere iniciar sesion primero ')
                  return redirect(url_for("home"))
            return f(*args, **kwargs)
      return decorated_function
