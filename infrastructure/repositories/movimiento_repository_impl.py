from typing import List
from sqlalchemy.orm import Session
from domain.entities.movimiento import Movimiento
from domain.repositories.movimiento_repository import MovimientoRepository
from infrastructure.database.models import MovimientoModel

class SQLAlchemyMovimientoRepository(MovimientoRepository):
    def __init__(self, db: Session):
        self.db = db

    def guardar(self, movimiento: Movimiento) -> None:
        movimiento_model = MovimientoModel(
            id=movimiento.id,
            material_id=movimiento.material_id,
            persona_cedula=movimiento.persona_cedula,
            persona_nombre=movimiento.persona_nombre,
            tipo=movimiento.tipo,
            fecha=movimiento.fecha
        )
        self.db.add(movimiento_model)
        self.db.commit()

    def obtener_todos(self) -> List[Movimiento]:
        movimientos_model = self.db.query(MovimientoModel).all()
        return [
            Movimiento(
                id=m.id,
                material_id=m.material_id,
                persona_cedula=m.persona_cedula,
                persona_nombre=m.persona_nombre,
                tipo=m.tipo,
                fecha=m.fecha
            )
            for m in movimientos_model
        ]

    def obtener_por_persona(self, cedula: str) -> List[Movimiento]:
        movimientos_model = self.db.query(MovimientoModel).filter(
            MovimientoModel.persona_cedula == cedula
        ).all()
        return [
            Movimiento(
                id=m.id,
                material_id=m.material_id,
                persona_cedula=m.persona_cedula,
                persona_nombre=m.persona_nombre,
                tipo=m.tipo,
                fecha=m.fecha
            )
            for m in movimientos_model
        ]

    def obtener_por_material(self, material_id: str) -> List[Movimiento]:
        movimientos_model = self.db.query(MovimientoModel).filter(
            MovimientoModel.material_id == material_id
        ).all()
        return [
            Movimiento(
                id=m.id,
                material_id=m.material_id,
                persona_cedula=m.persona_cedula,
                persona_nombre=m.persona_nombre,
                tipo=m.tipo,
                fecha=m.fecha
            )
            for m in movimientos_model
        ] 