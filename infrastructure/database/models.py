from sqlalchemy import Column, String, Integer, DateTime, Enum as SQLEnum
from infrastructure.database.database import Base
from domain.entities.persona import Rol
from domain.entities.movimiento import TipoMovimiento

class MaterialModel(Base):
    __tablename__ = "materiales"

    id = Column(String, primary_key=True)
    titulo = Column(String, nullable=False)
    fecha_registro = Column(DateTime, nullable=False)
    cantidad_registrada = Column(Integer, nullable=False)
    cantidad_actual = Column(Integer, nullable=False)

class PersonaModel(Base):
    __tablename__ = "personas"

    cedula = Column(String, primary_key=True)
    nombre = Column(String, nullable=False)
    rol = Column(SQLEnum(Rol), nullable=False)
    materiales_prestados = Column(String, nullable=False, default="[]")

class MovimientoModel(Base):
    __tablename__ = "movimientos"

    id = Column(String, primary_key=True)
    material_id = Column(String, nullable=False)
    persona_cedula = Column(String, nullable=False)
    persona_nombre = Column(String, nullable=False)
    tipo = Column(SQLEnum(TipoMovimiento), nullable=False)
    fecha = Column(DateTime, nullable=False) 