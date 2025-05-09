from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.persona import Persona

class PersonaRepository(ABC):
    @abstractmethod
    def guardar(self, persona: Persona) -> None:
        """Guarda una nueva persona en el repositorio."""
        pass

    @abstractmethod
    def obtener_por_cedula(self, cedula: str) -> Optional[Persona]:
        """Obtiene una persona por su cédula."""
        pass

    @abstractmethod
    def obtener_todas(self) -> List[Persona]:
        """Obtiene todas las personas."""
        pass

    @abstractmethod
    def actualizar(self, persona: Persona) -> None:
        """Actualiza una persona existente."""
        pass

    @abstractmethod
    def eliminar(self, cedula: str) -> None:
        """Elimina una persona del repositorio."""
        pass

    @abstractmethod
    def existe_cedula(self, cedula: str) -> bool:
        """Verifica si existe una persona con la cédula dada."""
        pass 