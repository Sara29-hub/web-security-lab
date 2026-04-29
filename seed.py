from models import Usuario, Base
from settings import engine, session as db_session

def Admin():
    Base.metadata.create_all(engine)

    usuario = Usuario(

        Nombre = "Admin1",
        Apellidos = "Backend",
        Email = "admin@gmai.com",
        Rol = "admin"

        )
    #Contraseña de ejemplo
    usuario.contraseña = "AdminPassword123!"

    db_session.add(usuario)
    db_session.commit()

if __name__ == '__main__':
    Admin()