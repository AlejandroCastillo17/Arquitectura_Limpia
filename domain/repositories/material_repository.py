from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.material import Material

class MaterialRepository(ABC):
    @abstractmethod
    def guardar(self, material: Material) -> None:
        """Guarda un nuevo material en el repositorio."""
        pass

    @abstractmethod
    def obtener_por_id(self, id: str) -> Optional[Material]:
        """Obtiene un material por su ID."""
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Material]:
        """Obtiene todos los materiales."""
        pass

    @abstractmethod
    def actualizar(self, material: Material) -> None:
        """Actualiza un material existente."""
        pass

    @abstractmethod
    def existe_id(self, id: str) -> bool:
        """Verifica si existe un material con el ID dado."""
        pass 