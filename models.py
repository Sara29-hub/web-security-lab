from sqlalchemy import Boolean, Column , ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from settings import engine
from settings import Base
from sqlalchemy import Date 
from settings import session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
from sqlalchemy.ext.hybrid import hybrid_property

class Usuario(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer(),primary_key= True, autoincrement=True)
    Nombre = Column(String(50), nullable=False)
    Apellidos = Column(String(80), nullable=False)
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
            "Created_at": self.Created_at
        }
    
    @hybrid_property
    def contraseña (self):
        raise AttributeError("La contraseña no es un atributo legible. ")
    



   
    @contraseña.setter
    def contraseña(self, contraseña_entexto):
        
        self.Contraseña_hash = bcrypt.generate_password_hash(contraseña_entexto).decode('utf-8')


    def autenticar(self, contraseña_entexto):
        return bcrypt.check_password_hash(self.Contraseña_hash, contraseña_entexto)


    



class Tarea(Base):
    __tablename__= 'Tarea'
    id = Column(Integer(),primary_key= True, autoincrement=True)
    Tarea_id = Column(Integer())
    usuario_id = Column(Integer(), ForeignKey("Usuario.id"), nullable=False)
    Nombre = Column(String(50), nullable=False)
    Fecha = Column(Date, nullable=False)
    Created_at = Column(DateTime(), default=datetime.now)
    Update_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    Contenido = Column(Text())

    def json(self):
        return {
            "id": self.id, 
            "usuario_id": self.usuario_id,
            "Nombre_tarea": self.Nombre,
            "Fecha": self.Fecha.isoformat() if self.Fecha else None,
            "Creado": self.Created_at.isoformat() if self.Created_at else None,
            "Actualizado_tarea": self.Update_at.isoformat() if self.Update_at else None,
            "Contendio_tarea": self.Contenido
        }



    

