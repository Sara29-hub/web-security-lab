from models import Usuario
from settings import session as db_session

def Admin():

    usuario = Usuario(

        Nombre = "Admin1",
        Apellidos = "Backend",
        Email = "admin@gmai.com",
        Rol = "admin"

        )
    usuario.contraseña = "Contraseña1234"

    db_session.add(usuario)
    db_session.commit()

if __name__ == '__main__':
    Admin()