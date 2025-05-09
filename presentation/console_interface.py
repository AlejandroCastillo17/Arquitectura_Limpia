from datetime import datetime
from typing import Optional
from infrastructure.database.database import SessionLocal, engine, Base
from infrastructure.repositories.material_repository_impl import SQLAlchemyMaterialRepository
from infrastructure.repositories.persona_repository_impl import SQLAlchemyPersonaRepository
from infrastructure.repositories.movimiento_repository_impl import SQLAlchemyMovimientoRepository
from application.use_cases.material_use_cases import MaterialUseCases
from application.use_cases.persona_use_cases import PersonaUseCases
from application.use_cases.movimiento_use_cases import MovimientoUseCases

class ConsoleInterface:
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = SessionLocal()
        
        # Initialize repositories
        self.material_repository = SQLAlchemyMaterialRepository(self.db)
        self.persona_repository = SQLAlchemyPersonaRepository(self.db)
        self.movimiento_repository = SQLAlchemyMovimientoRepository(self.db)
        
        # Initialize use cases
        self.material_use_cases = MaterialUseCases(self.material_repository)
        self.persona_use_cases = PersonaUseCases(self.persona_repository)
        self.movimiento_use_cases = MovimientoUseCases(
            self.movimiento_repository,
            self.material_repository,
            self.persona_repository
        )

    def mostrar_menu(self):
        print("\n=== Sistema de Gestión de Biblioteca ===")
        print("1. Registrar material")
        print("2. Registrar persona")
        print("3. Eliminar persona")
        print("4. Registrar préstamo")
        print("5. Registrar devolución")
        print("6. Incrementar cantidad de material")
        print("7. Consultar historial")
        print("0. Salir")
        return input("Seleccione una opción: ")

    def registrar_material(self):
        print("\n=== Registrar Material ===")
        id = input("ID del material: ")
        titulo = input("Título: ")
        cantidad = int(input("Cantidad: "))
        
        try:
            material = self.material_use_cases.registrar_material(id, titulo, cantidad)
            print(f"Material registrado exitosamente: {material.titulo}")
        except ValueError as e:
            print(f"Error: {str(e)}")

    def registrar_persona(self):
        print("\n=== Registrar Persona ===")
        nombre = input("Nombre: ")
        cedula = input("Cédula: ")
        print("Roles disponibles:")
        print("1. Estudiante")
        print("2. Profesor")
        print("3. Administrativo")
        rol_opcion = input("Seleccione el rol (1-3): ")
        
        roles = {
            "1": "estudiante",
            "2": "profesor",
            "3": "administrativo"
        }
        
        try:
            persona = self.persona_use_cases.registrar_persona(
                nombre, cedula, roles[rol_opcion]
            )
            print(f"Persona registrada exitosamente: {persona.nombre}")
        except (ValueError, KeyError) as e:
            print(f"Error: {str(e)}")

    def eliminar_persona(self):
        print("\n=== Eliminar Persona ===")
        cedula = input("Cédula de la persona a eliminar: ")
        
        try:
            self.persona_use_cases.eliminar_persona(cedula)
            print("Persona eliminada exitosamente")
        except ValueError as e:
            print(f"Error: {str(e)}")

    def registrar_prestamo(self):
        print("\n=== Registrar Préstamo ===")
        material_id = input("ID del material: ")
        cedula = input("Cédula de la persona: ")
        
        try:
            movimiento = self.movimiento_use_cases.registrar_prestamo(material_id, cedula)
            print(f"Préstamo registrado exitosamente para {movimiento.persona_nombre}")
        except ValueError as e:
            print(f"Error: {str(e)}")

    def registrar_devolucion(self):
        print("\n=== Registrar Devolución ===")
        material_id = input("ID del material: ")
        cedula = input("Cédula de la persona: ")
        
        try:
            movimiento = self.movimiento_use_cases.registrar_devolucion(material_id, cedula)
            print(f"Devolución registrada exitosamente para {movimiento.persona_nombre}")
        except ValueError as e:
            print(f"Error: {str(e)}")

    def incrementar_cantidad(self):
        print("\n=== Incrementar Cantidad de Material ===")
        material_id = input("ID del material: ")
        cantidad = int(input("Cantidad a incrementar: "))
        
        try:
            material = self.material_use_cases.incrementar_cantidad(material_id, cantidad)
            print(f"Cantidad incrementada exitosamente. Nueva cantidad: {material.cantidad_actual}")
        except ValueError as e:
            print(f"Error: {str(e)}")

    def consultar_historial(self):
        print("\n=== Consultar Historial ===")
        print("1. Historial completo")
        print("2. Historial por persona")
        print("3. Historial por material")
        opcion = input("Seleccione una opción (1-3): ")
        
        try:
            if opcion == "1":
                movimientos = self.movimiento_use_cases.obtener_historial()
            elif opcion == "2":
                cedula = input("Cédula de la persona: ")
                movimientos = self.movimiento_use_cases.obtener_historial_persona(cedula)
            elif opcion == "3":
                material_id = input("ID del material: ")
                movimientos = self.movimiento_use_cases.obtener_historial_material(material_id)
            else:
                print("Opción inválida")
                return

            print("\nHistorial de movimientos:")
            for m in movimientos:
                print(f"Fecha: {m.fecha}")
                print(f"Tipo: {m.tipo.value}")
                print(f"Material ID: {m.material_id}")
                print(f"Persona: {m.persona_nombre} ({m.persona_cedula})")
                print("-" * 50)
        except ValueError as e:
            print(f"Error: {str(e)}")

    def ejecutar(self):
        while True:
            opcion = self.mostrar_menu()
            
            if opcion == "1":
                self.registrar_material()
            elif opcion == "2":
                self.registrar_persona()
            elif opcion == "3":
                self.eliminar_persona()
            elif opcion == "4":
                self.registrar_prestamo()
            elif opcion == "5":
                self.registrar_devolucion()
            elif opcion == "6":
                self.incrementar_cantidad()
            elif opcion == "7":
                self.consultar_historial()
            elif opcion == "0":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida") 