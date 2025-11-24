from sqlalchemy import Boolean, Column , ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from settings import engine
from settings import Base
from settings import session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
from sqlalchemy.ext.hybrid import hybrid_property

class Usuario(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer(),primary_key= True, autoincrement=True)
    Nombre = Column(String(50), nullable=False, unique=True)
    Apellidos = Column(String(80), nullable=False, unique=True)
    Contraseña_hash = Column(String(128), nullable=False)
    Email = Column(String(50), nullable=False, unique=True)
    Created_at = Column(DateTime(), default=datetime.now)
    Rol = Column(String(50) )

    def json(self):
        return {
            "id": self.id,
            "Nombre": self.Nombre,
            "Apellidos": self.Apellidos,
            "Email": self.Email,
            "Rol": self.Rol,
            "Contraseña": self.Contraseña_hash,
            "Created_at": self.Created_at
        }
    
    @hybrid_property
    def contraseña (self):
        raise AttributeError("La contraseña no es un atributo legible. ")
        


    @contraseña.setter
    def contraseña (self, contraseña_entexto):
        
        codigo_Bytes = contraseña_entexto.encode('utf-8')

        hashed_bytes = bcrypt.generate_password_hash(codigo_Bytes)

        self.Contraseña_hash = hashed_bytes.decode('utf-8')


        

    def autenticar(self, contraseña_entexto):
        return bcrypt.check_password_hash(self.Contraseña_hash, contraseña_entexto)

    



class Tarea(Base):
    __tablename__= 'Tarea'
    id = Column(Integer(),primary_key= True)
    Tarea_id = Column(Integer())
    Nombre = Column(String(50), nullable=False, unique=True)
    Created_at = Column(DateTime(), default=datetime.now)
    Update_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    Contenido = Column(Text())

    def json(self):
        return {
            "id": self.id, 
            "Nombre_tarea": self.Nombre,
            "Creado": self.Created_at,
            "Actualizado_tarea": self.Update_at,
            "Contendio_tarea": self.Contenido
        }


if __name__ == '__main__':

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    user1 = Usuario(Nombre = "Sara", Apellidos= "Lo que sea", Email= "Holaaa29@gmail.com", Rol = "Administradora" )
    Tarea1 = Tarea(id = 1, Nombre = " Apuntes", Contenido= " Intentando hace mas cosas sin saturarme ")

    session.add(user1)
    session.add(Tarea1)

    session.commit()
