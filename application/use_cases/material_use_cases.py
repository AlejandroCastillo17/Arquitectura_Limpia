from datetime import datetime
from typing import List
from domain.entities.material import Material
from domain.repositories.material_repository import MaterialRepository

class MaterialUseCases:
    def __init__(self, material_repository: MaterialRepository):
        self.material_repository = material_repository

    def registrar_material(self, id: str, titulo: str, cantidad: int) -> Material:
        """Registra un nuevo material en el catálogo."""
        if self.material_repository.existe_id(id):
            raise ValueError("Ya existe un material con ese ID")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")

        material = Material(
            id=id,
            titulo=titulo,
            fecha_registro=datetime.now(),
            cantidad_registrada=cantidad,
            cantidad_actual=cantidad
        )
        
        self.material_repository.guardar(material)
        return material

    def incrementar_cantidad(self, id: str, cantidad: int) -> Material:
        """Incrementa la cantidad de un material."""
        material = self.material_repository.obtener_por_id(id)
        if not material:
            raise ValueError("No existe un material con ese ID")

        material.incrementar_cantidad(cantidad)
        self.material_repository.actualizar(material)
        return material

    def obtener_material(self, id: str) -> Material:
        """Obtiene un material por su ID."""
        material = self.material_repository.obtener_por_id(id)
        if not material:
            raise ValueError("No existe un material con ese ID")
        return material

    def obtener_todos_materiales(self) -> List[Material]:
        """Obtiene todos los materiales."""
        return self.material_repository.obtener_todos() 