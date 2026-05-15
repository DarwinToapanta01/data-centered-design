# Servicios ORM con Python

API REST construida con **Flask** y **SQLAlchemy** que implementa el patrón **Repository** para gestionar autores y papers académicos.

## Tecnologías

- Python 3.10
- Flask
- SQLAlchemy (ORM)
- SQLite

## Estructura del proyecto

```
servicios-orm-py/
├── app.py                      # Punto de entrada
├── config/
│   └── configuracion.py        # Configuración de la app y base de datos
├── models/
│   ├── autor.py                # Modelo Autor
│   └── paper.py                # Modelo Paper
├── repository/
│   ├── repositorio_base.py     # Repositorio genérico (CRUD)
│   ├── repositorio_autor.py    # Repositorio de autores
│   └── repositorio_paper.py    # Repositorio de papers
└── routes/
    ├── autor.py                # Rutas /autores
    └── paper.py                # Rutas /papers
```

## Instalación

```bash
pip install flask flask-sqlalchemy
python app.py
```

La app corre en `http://localhost:500`.

## Endpoints

### Autores `/autores`

| Método | Ruta           | Descripción      |
|--------|----------------|------------------|
| GET    | `/autores/`    | Listar todos     |
| POST   | `/autores/`    | Crear autor      |
| PUT    | `/autores/:id` | Actualizar autor |
| DELETE | `/autores/:id` | Eliminar autor   |

**POST / PUT body:**
```json
{ "nombre": "Juan Pérez", "pais": "Ecuador" }
```

### Papers `/papers`

| Método | Ruta          | Descripción      |
|--------|---------------|------------------|
| GET    | `/papers/`    | Listar todos     |
| POST   | `/papers/`    | Crear paper      |
| PUT    | `/papers/:id` | Actualizar paper |
| DELETE | `/papers/:id` | Eliminar paper   |

**POST / PUT body:**
```json
{ "titulo": "Mi paper", "doi": "10.1234/ejemplo", "id_autor": 1 }
```

## Patrón Repository

Todos los accesos a la base de datos pasan por `RepositorioBase`, que encapsula las operaciones CRUD. Los repositorios específicos (`RepositorioAutor`, `RepositorioPaper`) extienden esta clase base.

```
RepositorioBase
├── obtener_todos()
├── obtener_por_id(id)
├── crear(objeto)
├── actualizar()
└── eliminar(objeto)
```
