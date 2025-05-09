from dataclasses import dataclass
from enum import Enum
from typing import List

class Rol(Enum):
    ESTUDIANTE = "estudiante"
    PROFESOR = "profesor"
    ADMINISTRATIVO = "administrativo"

@dataclass
class Persona:
    nombre: str
    cedula: str
    rol: Rol
    materiales_prestados: List[str] = None

    def __post_init__(self):
        if self.materiales_prestados is None:
            self.materiales_prestados = []

    @property
    def limite_prestamos(self) -> int:
        """Retorna el límite de préstamos según el rol."""
        limites = {
            Rol.ESTUDIANTE: 5,
            Rol.PROFESOR: 3,
            Rol.ADMINISTRATIVO: 1
        }
        return limites[self.rol]

    def puede_prestar(self) -> bool:
        """Verifica si la persona puede prestar más materiales."""
        return len(self.materiales_prestados) < self.limite_prestamos

    def prestar_material(self, material_id: str) -> None:
        """Registra el préstamo de un material."""
        if not self.puede_prestar():
            raise ValueError(f"No se pueden prestar más materiales. Límite alcanzado: {self.limite_prestamos}")
        if material_id in self.materiales_prestados:
            raise ValueError("El material ya está prestado a esta persona")
        self.materiales_prestados.append(material_id)

    def devolver_material(self, material_id: str) -> None:
        """Registra la devolución de un material."""
        if material_id not in self.materiales_prestados:
            raise ValueError("El material no está prestado a esta persona")
        self.materiales_prestados.remove(material_id)

    def tiene_materiales_prestados(self) -> bool:
        """Verifica si la persona tiene materiales prestados."""
        return len(self.materiales_prestados) > 0 