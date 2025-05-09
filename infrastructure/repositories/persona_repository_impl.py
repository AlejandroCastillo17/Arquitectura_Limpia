import json
from typing import List, Optional
from sqlalchemy.orm import Session
from domain.entities.persona import Persona
from domain.repositories.persona_repository import PersonaRepository
from infrastructure.database.models import PersonaModel

class SQLAlchemyPersonaRepository(PersonaRepository):
    def __init__(self, db: Session):
        self.db = db

    def guardar(self, persona: Persona) -> None:
        persona_model = PersonaModel(
            cedula=persona.cedula,
            nombre=persona.nombre,
            rol=persona.rol,
            materiales_prestados=json.dumps(persona.materiales_prestados)
        )
        self.db.add(persona_model)
        self.db.commit()

    def obtener_por_cedula(self, cedula: str) -> Optional[Persona]:
        persona_model = self.db.query(PersonaModel).filter(PersonaModel.cedula == cedula).first()
        if not persona_model:
            return None
        
        return Persona(
            nombre=persona_model.nombre,
            cedula=persona_model.cedula,
            rol=persona_model.rol,
            materiales_prestados=json.loads(persona_model.materiales_prestados)
        )

    def obtener_todas(self) -> List[Persona]:
        personas_model = self.db.query(PersonaModel).all()
        return [
            Persona(
                nombre=p.nombre,
                cedula=p.cedula,
                rol=p.rol,
                materiales_prestados=json.loads(p.materiales_prestados)
            )
            for p in personas_model
        ]

    def actualizar(self, persona: Persona) -> None:
        persona_model = self.db.query(PersonaModel).filter(PersonaModel.cedula == persona.cedula).first()
        if persona_model:
            persona_model.nombre = persona.nombre
            persona_model.rol = persona.rol
            persona_model.materiales_prestados = json.dumps(persona.materiales_prestados)
            self.db.commit()

    def eliminar(self, cedula: str) -> None:
        persona_model = self.db.query(PersonaModel).filter(PersonaModel.cedula == cedula).first()
        if persona_model:
            self.db.delete(persona_model)
            self.db.commit()

    def existe_cedula(self, cedula: str) -> bool:
        return self.db.query(PersonaModel).filter(PersonaModel.cedula == cedula).first() is not None 