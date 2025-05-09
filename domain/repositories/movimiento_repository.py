from abc import ABC, abstractmethod
from typing import List
from domain.entities.movimiento import Movimiento

class MovimientoRepository(ABC):
    @abstractmethod
    def guardar(self, movimiento: Movimiento) -> None:
        """Guarda un nuevo movimiento en el repositorio."""
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Movimiento]:
        """Obtiene todos los movimientos."""
        pass

    @abstractmethod
    def obtener_por_persona(self, cedula: str) -> List[Movimiento]:
        """Obtiene todos los movimientos de una persona."""
        pass

    @abstractmethod
    def obtener_por_material(self, material_id: str) -> List[Movimiento]:
        """Obtiene todos los movimientos de un material."""
        pass 