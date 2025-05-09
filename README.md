# Sistema de Gestión de Biblioteca

Este proyecto implementa un sistema de gestión de biblioteca utilizando Arquitectura Limpia (Clean Architecture).

## Estructura del Proyecto

El proyecto está organizado en las siguientes capas:

- **Domain**: Contiene las entidades y reglas de negocio centrales
- **Application**: Contiene los casos de uso y la lógica de aplicación
- **Infrastructure**: Implementa la persistencia y servicios externos
- **Presentation**: Maneja la interfaz de usuario

## Requisitos

- **Python 3.11** (IMPORTANTE: No es compatible con Python 3.13)
- pip (gestor de paquetes de Python)

## Instalación y Configuración

1. **Instalar Python 3.11**:
   - Descargar Python 3.11 desde [python.org](https://www.python.org/downloads/release/python-3110/)
   - Durante la instalación, marcar la opción "Add Python to PATH"

2. **Clonar el repositorio**:
```bash
git clone <url-del-repositorio>
cd Arquitectura_Limpia
```

3. **Crear entorno virtual**:
```bash
# Crear el entorno virtual
py -3.11 -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

4. **Instalar dependencias**:
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

## Notas Importantes

- La base de datos SQLite se creará automáticamente al ejecutar la aplicación por primera vez
- **IMPORTANTE**: El proyecto requiere específicamente Python 3.11. No funcionará con Python 3.13
- El entorno virtual debe estar activado cada vez que trabajes con el proyecto
- Si encuentras algún error, verifica que todas las dependencias se hayan instalado correctamente

## Solución de Problemas

Si encuentras el error:
```
AssertionError: Class <class 'sqlalchemy.sql.elements.SQLCoreOperations'> directly inherits TypingOnly but has additional attributes
```

Esto significa que estás usando una versión incorrecta de Python. Sigue estos pasos:

1. Desinstala Python 3.13 si lo tienes instalado
2. Instala Python 3.11 desde [python.org](https://www.python.org/downloads/release/python-3110/)
3. Elimina el entorno virtual actual:
   ```bash
   deactivate
   rm -r venv
   ```
4. Crea un nuevo entorno virtual con Python 3.11:
   ```bash
   py -3.11 -m venv venv
   venv\Scripts\activate
   ```
5. Reinstala las dependencias:
   ```bash
   pip install -r requirements.txt
   ``` 

##  en caso de no entener colocar estos comandos
deactivate

# En Windows PowerShell:
Remove-Item -Recurse -Force venv

py -3.11 --version

# asegurece profe  de usar py -3.11 explícitamente
py -3.11 -m venv venv

.\venv\Scripts\activate

python --version

pip install -r requirements.txt

python main.py