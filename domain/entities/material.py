from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Material:
    id: str
    titulo: str
    fecha_registro: datetime
    cantidad_registrada: int
    cantidad_actual: int

    def incrementar_cantidad(self, cantidad: int) -> None:
        """Incrementa la cantidad registrada y actual del material."""
        if cantidad <= 0:
            raise ValueError("La cantidad a incrementar debe ser mayor a 0")
        self.cantidad_registrada += cantidad
        self.cantidad_actual += cantidad

    def prestar(self) -> None:
        """Registra el préstamo de una unidad del material."""
        if self.cantidad_actual <= 0:
            raise ValueError("No hay unidades disponibles para prestar")
        self.cantidad_actual -= 1

    def devolver(self) -> None:
        """Registra la devolución de una unidad del material."""
        if self.cantidad_actual >= self.cantidad_registrada:
            raise ValueError("No se pueden devolver más unidades de las registradas")
        self.cantidad_actual += 1 