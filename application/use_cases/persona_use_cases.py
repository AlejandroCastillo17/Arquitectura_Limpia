from typing import List
from domain.entities.persona import Persona, Rol
from domain.repositories.persona_repository import PersonaRepository

class PersonaUseCases:
    def __init__(self, persona_repository: PersonaRepository):
        self.persona_repository = persona_repository

    def registrar_persona(self, nombre: str, cedula: str, rol: str) -> Persona:
        """Registra una nueva persona."""
        if self.persona_repository.existe_cedula(cedula):
            raise ValueError("Ya existe una persona con esa cédula")

        try:
            rol_enum = Rol(rol.lower())
        except ValueError:
            raise ValueError("Rol inválido. Debe ser: estudiante, profesor o administrativo")

        persona = Persona(
            nombre=nombre,
            cedula=cedula,
            rol=rol_enum
        )
        
        self.persona_repository.guardar(persona)
        return persona

    def eliminar_persona(self, cedula: str) -> None:
        """Elimina una persona del registro."""
        persona = self.persona_repository.obtener_por_cedula(cedula)
        if not persona:
            raise ValueError("No existe una persona con esa cédula")

        if persona.tiene_materiales_prestados():
            raise ValueError("No se puede eliminar una persona con materiales prestados")

        self.persona_repository.eliminar(cedula)

    def obtener_persona(self, cedula: str) -> Persona:
        """Obtiene una persona por su cédula."""
        persona = self.persona_repository.obtener_por_cedula(cedula)
        if not persona:
            raise ValueError("No existe una persona con esa cédula")
        return persona

    def obtener_todas_personas(self) -> List[Persona]:
        """Obtiene todas las personas."""
        return self.persona_repository.obtener_todas() 