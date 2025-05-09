from typing import List, Optional
from sqlalchemy.orm import Session
from domain.entities.material import Material
from domain.repositories.material_repository import MaterialRepository
from infrastructure.database.models import MaterialModel

class SQLAlchemyMaterialRepository(MaterialRepository):
    def __init__(self, db: Session):
        self.db = db

    def guardar(self, material: Material) -> None:
        material_model = MaterialModel(
            id=material.id,
            titulo=material.titulo,
            fecha_registro=material.fecha_registro,
            cantidad_registrada=material.cantidad_registrada,
            cantidad_actual=material.cantidad_actual
        )
        self.db.add(material_model)
        self.db.commit()

    def obtener_por_id(self, id: str) -> Optional[Material]:
        material_model = self.db.query(MaterialModel).filter(MaterialModel.id == id).first()
        if not material_model:
            return None
        
        return Material(
            id=material_model.id,
            titulo=material_model.titulo,
            fecha_registro=material_model.fecha_registro,
            cantidad_registrada=material_model.cantidad_registrada,
            cantidad_actual=material_model.cantidad_actual
        )

    def obtener_todos(self) -> List[Material]:
        materiales_model = self.db.query(MaterialModel).all()
        return [
            Material(
                id=m.id,
                titulo=m.titulo,
                fecha_registro=m.fecha_registro,
                cantidad_registrada=m.cantidad_registrada,
                cantidad_actual=m.cantidad_actual
            )
            for m in materiales_model
        ]

    def actualizar(self, material: Material) -> None:
        material_model = self.db.query(MaterialModel).filter(MaterialModel.id == material.id).first()
        if material_model:
            material_model.titulo = material.titulo
            material_model.fecha_registro = material.fecha_registro
            material_model.cantidad_registrada = material.cantidad_registrada
            material_model.cantidad_actual = material.cantidad_actual
            self.db.commit()

    def existe_id(self, id: str) -> bool:
        return self.db.query(MaterialModel).filter(MaterialModel.id == id).first() is not None 