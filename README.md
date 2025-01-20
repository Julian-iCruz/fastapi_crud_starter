# FastAPI Project Template

This repository is a template for starting projects with **FastAPI**, with Docker configuration and dependency management using **Poetry**.  
> Este repositorio es una plantilla para iniciar proyectos con **FastAPI**, con configuración para Docker y gestión de dependencias usando **Poetry**.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#clone-the-repository)
    - [Using Docker Compose](#using-docker-compose)
        - [Start in the Production Environment](#start-in-the-production-environment)
        - [Start in the Development Environment (with Debugging)](#start-in-the-development-environment-with-debugging)
    - [Install Dependencies](#install-dependencies)
    - [Run the Development Server](#run-the-development-server)

---

## Project Structure

The project includes a basic configuration for a **FastAPI** API and configuration files for Docker. Below is a description of the project structure and configuration.  
> El proyecto incluye una configuración básica para una API en **FastAPI** y archivos de configuración para Docker. A continuación, se describe la estructura y configuración del proyecto.

### Key Files:

- `pyproject.toml`: Poetry project configuration, including dependencies and development environment setup.  
  > Configuración del proyecto con Poetry, incluyendo dependencias y configuración para el entorno de desarrollo.
- `docker-compose.yml`: Docker Compose configuration file for setting up the project environment.  
  > Archivo de configuración para iniciar el proyecto utilizando Docker y Docker Compose.
- `dockerfiles/`: Folder containing two Dockerfiles, one for development and one for production.  
  > Carpeta que contiene dos Dockerfiles, uno para un entorno de desarrollo y otro para el entorno de producción.
- `app/main.py`: The main file with the **FastAPI** application setup.  
  > El archivo principal con la configuración de la API en **FastAPI**.

---

## Installation

### Prerequisites

1. Have **Docker** and **Docker Compose** installed.  
   > Tener **Docker** y **Docker Compose** instalados.
2. Have **Poetry** installed on your machine for dependency management.  
   > Tener **Poetry** instalado en tu máquina para la gestión de dependencias.

### Clone the Repository

```bash
git clone https://github.com/user/fastapi-project-template.git
cd fastapi-project-template
```
> Clona el repositorio y accede al directorio del proyecto.

---

### Using Docker Compose

You can bring up the project containers using Docker Compose, which will use the `docker-compose.yml` and corresponding Dockerfiles to set up the development and production environments.  
> Puedes levantar los contenedores del proyecto con Docker Compose, que utilizará el archivo `docker-compose.yml` y los Dockerfiles correspondientes para configurar los entornos de desarrollo y producción.

#### Start in the Production Environment

```bash
docker-compose up fastapi-project-template
```
> Inicia el entorno de producción con el siguiente comando.

#### Start in the Development Environment (with Debugging)

```bash
docker-compose up fastapi-project-template-debug
```
> Inicia el entorno de desarrollo (con soporte para depuración) con el siguiente comando.

---

### Install Dependencies

If you want to install dependencies locally instead of using Docker, you can do it with Poetry:  
> Si deseas instalar las dependencias localmente en lugar de usar Docker, puedes hacerlo con Poetry:

```bash
poetry install --no-root
```

---

### Run the Development Server

To run the FastAPI server directly, use the following command:  
> Para ejecutar el servidor de FastAPI directamente, usa el siguiente comando:

```bash
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```
