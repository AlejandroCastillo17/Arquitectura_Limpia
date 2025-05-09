# Sistema de Gestión de Biblioteca

Este proyecto implementa un sistema de gestión de biblioteca utilizando Arquitectura Limpia (Clean Architecture).

## Estructura del Proyecto

El proyecto está organizado en las siguientes capas:

- **Domain**: Contiene las entidades y reglas de negocio centrales
- **Application**: Contiene los casos de uso y la lógica de aplicación
- **Infrastructure**: Implementa la persistencia y servicios externos
- **Presentation**: Maneja la interfaz de usuario

## Requisitos

- Python 3.8+
- SQLite3

## Instalación

1. Clonar el repositorio
2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar el programa:

```bash
python main.py
```

## Funcionalidades

1. Registrar material en el catálogo
2. Registrar persona
3. Eliminar persona
4. Registrar préstamo
5. Registrar devolución
6. Incrementar cantidad de material
7. Consultar historial de la biblioteca 