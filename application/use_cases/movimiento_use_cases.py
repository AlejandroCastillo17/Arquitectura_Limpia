from datetime import datetime
import uuid
from typing import List
from domain.entities.movimiento import Movimiento, TipoMovimiento
from domain.repositories.material_repository import MaterialRepository
from domain.repositories.persona_repository import PersonaRepository
from domain.repositories.movimiento_repository import MovimientoRepository

class MovimientoUseCases:
    def __init__(
        self,
        movimiento_repository: MovimientoRepository,
        material_repository: MaterialRepository,
        persona_repository: PersonaRepository
    ):
        self.movimiento_repository = movimiento_repository
        self.material_repository = material_repository
        self.persona_repository = persona_repository

    def registrar_prestamo(self, material_id: str, cedula: str) -> Movimiento:
        """Registra un préstamo de material."""
        material = self.material_repository.obtener_por_id(material_id)
        if not material:
            raise ValueError("No existe un material con ese ID")

        persona = self.persona_repository.obtener_por_cedula(cedula)
        if not persona:
            raise ValueError("No existe una persona con esa cédula")

        if not persona.puede_prestar():
            raise ValueError(f"No se pueden prestar más materiales. Límite alcanzado: {persona.limite_prestamos}")

        material.prestar()
        persona.prestar_material(material_id)

        movimiento = Movimiento(
            id=str(uuid.uuid4()),
            material_id=material_id,
            persona_cedula=cedula,
            persona_nombre=persona.nombre,
            tipo=TipoMovimiento.PRESTAMO,
            fecha=datetime.now()
        )

        self.material_repository.actualizar(material)
        self.persona_repository.actualizar(persona)
        self.movimiento_repository.guardar(movimiento)

        return movimiento

    def registrar_devolucion(self, material_id: str, cedula: str) -> Movimiento:
        """Registra una devolución de material."""
        material = self.material_repository.obtener_por_id(material_id)
        if not material:
            raise ValueError("No existe un material con ese ID")

        persona = self.persona_repository.obtener_por_cedula(cedula)
        if not persona:
            raise ValueError("No existe una persona con esa cédula")

        material.devolver()
        persona.devolver_material(material_id)

        movimiento = Movimiento(
            id=str(uuid.uuid4()),
            material_id=material_id,
            persona_cedula=cedula,
            persona_nombre=persona.nombre,
            tipo=TipoMovimiento.DEVOLUCION,
            fecha=datetime.now()
        )

        self.material_repository.actualizar(material)
        self.persona_repository.actualizar(persona)
        self.movimiento_repository.guardar(movimiento)

        return movimiento

    def obtener_historial(self) -> List[Movimiento]:
        """Obtiene el historial completo de movimientos."""
        return self.movimiento_repository.obtener_todos()

    def obtener_historial_persona(self, cedula: str) -> List[Movimiento]:
        """Obtiene el historial de movimientos de una persona."""
        return self.movimiento_repository.obtener_por_persona(cedula)

    def obtener_historial_material(self, material_id: str) -> List[Movimiento]:
        """Obtiene el historial de movimientos de un material."""
        return self.movimiento_repository.obtener_por_material(material_id) 