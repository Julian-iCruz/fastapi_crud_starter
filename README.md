# FastAPI CRUD Starter

Welcome to FastAPI CRUD Starter! This project is a basic template to start developing CRUD (Create, Read, Update, Delete) applications using FastAPI, SQLAlchemy, and Alembic with Docker containers.

> ¡Bienvenido a FastAPI CRUD Starter! Este proyecto es una plantilla básica para comenzar a desarrollar aplicaciones CRUD (Crear, Leer, Actualizar, Eliminar) utilizando FastAPI, SQLAlchemy, y Alembic con contenedores Docker.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Set Environment Variables](#set-environment-variables)
- [Configuration](#configuration)
- [Start the Project](#start-the-project)
- [Migrations](#migrations)
  - [Create a Migration](#create-a-migration)
  - [Apply Migrations](#apply-migrations)
- [Usage](#usage)
  - [Access the API](#access-the-api)
  - [API Documentation](#api-documentation)
  - [Manage the Database with PgAdmin](#manage-the-database-with-pgadmin)
- [Contribution](#contribution)
- [License](#license)

## Features

- **FastAPI:** Modern and fast framework for building APIs with Python.
- **SQLAlchemy:** Powerful and flexible ORM to manage the database.
- **Alembic:** Migration tool to manage database schema changes.
- **Docker Compose:** Facilitates container orchestration for development and deployment.
- **PgAdmin:** Graphical interface to manage the PostgreSQL database.

> - **FastAPI:** Framework moderno y rápido para construir APIs con Python.
> - **SQLAlchemy:** ORM potente y flexible para manejar la base de datos.
> - **Alembic:** Herramienta de migraciones para gestionar cambios en el esquema de la base de datos.
> - **Docker Compose:** Facilita la orquestación de contenedores para el desarrollo y despliegue.
> - **PgAdmin:** Interfaz gráfica para gestionar la base de datos PostgreSQL.

## Technologies Used

- Python 3.12
- FastAPI
- SQLAlchemy
- Alembic
- Poetry
- Docker & Docker Compose
- PostgreSQL
- PgAdmin

## Project Structure

```plaintext
fastapi-crud-starter/
├── app/
│   ├── alembic.ini
│   ├── migrations/
│   │   ├── env.py
│   │   └── versions/
│   │       ├── 7132989f72ee_my_first_migration.py
│   │       ├── 48e990622d09_add_status_field.py
│   │       └── cc5eda956633_delete_status_field.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── models.py
│   │   └── session.py
│   ├── routers/
│   │   └── items.py
│   ├── schemas/
│   │   └── item.py
│   └── main.py
├── docker-compose.yml
├── dockerfiles/
│   ├── dockerfile.local
│   └── dockerfile.debug
├── pyproject.toml
├── poetry.lock
├── .env
└── .gitignore
```

## Requirements

- Docker and Docker Compose installed on your machine.
- Poetry installed globally if you wish to manage dependencies outside Docker.

> - Docker y Docker Compose instalados en tu máquina.
> - Poetry instalado globalmente si deseas manejar dependencias fuera de Docker.

## Installation

### Clone the Repository

Clone the repository on your local machine and navigate to the project directory.
> Clona el repositorio en tu máquina local y navega al directorio del proyecto.

```bash
git clone https://github.com/tu-usuario/fastapi-crud-starter.git
cd fastapi-crud-starter
```

### Set Environment Variables

Create a `.env` file in the project root based on `.env.example` (if available) or define the required variables:
> Cree un archivo `.env` en la raíz del proyecto basado en `.env.example` (si está disponible) o defina las variables necesarias:

```env
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

PGADMIN_DEFAULT_EMAIL=user@mail.com
PGADMIN_DEFAULT_PASSWORD=Temporal123*
PGADMIN_SERVER_JSON_FILE=/servers.json
POSTGRES_LOCAL_DATA_PATH=/postgres_data
```

Additionally, create a `servers.json` file with the following content to automatically add the server in PgAdmin:
> Además, cree un archivo `servers.json` con el siguiente contenido para añadir automáticamente el servidor en PgAdmin:

```json
{
    "Servers": {
        "1": {
            "Name": "name_db",
            "Group": "group_db",
            "Host": "postgres",
            "Port": 5432,
            "MaintenanceDB": "postgres_db",
            "Username": "postgres_user",
            "SSLMode": "prefer"
        }
    }
}
```

Save this file at the path defined by `PGADMIN_SERVER_JSON_FILE` (default: `/servers.json`).
> Guarda este archivo en la ruta definida por `PGADMIN_SERVER_JSON_FILE` (por defecto: `/servers.json`).

## Configuration

Ensure that the environment variables in `.env` are correctly set for your development environment. Specifically, `POSTGRES_HOST` should be `postgres` when working inside Docker and `localhost` if running commands from your local machine.
> Asegúrate de que las variables de entorno en `.env` estén configuradas correctamente para tu entorno de desarrollo. En particular, `POSTGRES_HOST` debe ser `postgres` cuando trabajes dentro de Docker y `localhost` si ejecutas comandos desde tu máquina local.

## Start the Project

To start all the services defined in `docker-compose.yml`:
> Para iniciar todos los servicios definidos en `docker-compose.yml`:

```bash
docker-compose up --build
```

This will start the following services:

- `postgres_db`: PostgreSQL database.
- `pgadmin`: Graphical interface for PostgreSQL.
- `migrations`: Service to apply Alembic migrations.
- `fastapi-crud-starter`: FastAPI application.
- `fastapi-crud-starter-debug`: Debug version of the application.

> Esto iniciará los siguientes servicios:
> - `postgres_db`: Base de datos PostgreSQL.
> - `pgadmin`: Interfaz gráfica para PostgreSQL.
> - `migrations`: Servicio encargado de aplicar las migraciones de Alembic.
> - `fastapi-crud-starter`: Aplicación FastAPI.
> - `fastapi-crud-starter-debug`: Versión de la aplicación con soporte para depuración.

## Migrations

### Create a Migration

To create a new migration after modifying your models:
> Para crear una nueva migración después de modificar sus modelos:

#### Run the Migration Command

Run it from your local machine (ensuring `POSTGRES_HOST=localhost`):
> Ejecútelo desde su máquina local (asegurándose de que `POSTGRES_HOST=localhost`):

```bash
POSTGRES_HOST=localhost poetry run alembic revision --autogenerate -m "Description of the migration"
```

### Apply Migrations

To apply all pending migrations:
> Para aplicar todas las migraciones pendientes:

Run it from your local machine:
> Ejecútalo desde tu máquina local:

```bash
POSTGRES_HOST=localhost poetry run alembic upgrade head
```

## Usage

### Access the API

Once all services are running, you can access the API at: [http://localhost:8080](http://localhost:8080)

> Una vez que todos los servicios estén en funcionamiento, puedes acceder a la API en: [http://localhost:8080](http://localhost:8080).

### API Documentation

FastAPI automatically generates interactive documentation, which can be accessed at:
> FastAPI genera automáticamente documentación interactiva, a la que puedes acceder en:

- [Swagger UI](http://localhost:8080/docs)
- [ReDoc](http://localhost:8080/redoc)


### Manage the Database with PgAdmin

Access PgAdmin at [http://localhost:80](http://localhost:80) using the credentials defined in your `.env` file (`PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD`).

> Accede a PgAdmin en [http://localhost:80](http://localhost:80) usando las credenciales definidas en tu archivo `.env` (`PGADMIN_DEFAULT_EMAIL` y `PGADMIN_DEFAULT_PASSWORD`).

## Contribution

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

> ¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request con tus mejoras.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

> Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
