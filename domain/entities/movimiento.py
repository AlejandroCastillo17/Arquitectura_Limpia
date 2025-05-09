from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class TipoMovimiento(Enum):
    PRESTAMO = "prestamo"
    DEVOLUCION = "devolucion"

@dataclass
class Movimiento:
    id: str
    material_id: str
    persona_cedula: str
    persona_nombre: str
    tipo: TipoMovimiento
    fecha: datetime 