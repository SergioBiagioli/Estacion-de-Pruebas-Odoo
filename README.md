# Estación de Desarrollo Odoo 18 con Docker

Este proyecto contiene una estación de trabajo completa para desarrollar y probar módulos en Odoo 18, utilizando Docker y PostgreSQL. Todo el entorno está encapsulado, lo que permite correrlo fácilmente en cualquier máquina con Docker instalado.

---

## 🚀 Requisitos

- [Docker Desktop](https://www.docker.com/get-started/) instalado y funcionando (con soporte para WSL2 en Windows)
- Git (opcional, para clonar el proyecto)
- Visual Studio Code (opcional, recomendado para desarrollo)

---

## 📆 Estructura del proyecto

```
odoo-dev/
├── odoo/               # Repositorio clonado de Odoo Community
├── custom_addons/      # Tus propios módulos
├── config/
│   └── odoo.conf       # Configuración de Odoo
└── docker-compose.yml  # Orquestador de servicios
```

---

## 🧰 Primer uso

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/mi-proyecto-odoo.git
   cd mi-proyecto-odoo
   ```

2. Levantar los servicios:

   ```bash
   docker compose up -d
   ```

3. Acceder desde el navegador: [http://localhost:8069](http://localhost:8069)

4. Crear una nueva base de datos:

   - Master password: `admin` (o la definida en `odoo.conf`)

---

## 🐐 Base de datos

La base de datos es un contenedor PostgreSQL totalmente independiente de tu sistema local. No necesitás instalar PostgreSQL por separado.

---

## 🛠 Desarrollo

- Podés colocar tus módulos en la carpeta `custom_addons/`
- El archivo `odoo.conf` ya está configurado para cargar módulos desde allí
- Reiniciar el servidor para ver los cambios:

  ```bash
  docker compose restart web
  ```

---

## 🧼 Detener todo

```bash
docker compose down
```

Esto detendrá los contenedores sin borrar los datos.

---

## 🔁 Restaurar una base de datos

Podés usar la opción "restore a database" desde la pantalla principal de Odoo y cargar un `.zip` exportado desde Odoo.sh u otro entorno.

---

# Odoo 18 Development Environment with Docker

This project includes a fully encapsulated development and testing environment for Odoo 18 using Docker and PostgreSQL. It can be run easily on any machine that has Docker installed.

---

## 🚀 Requirements

- [Docker Desktop](https://www.docker.com/get-started/) installed and running (with WSL2 support on Windows)
- Git (optional, to clone the project)
- Visual Studio Code (optional, recommended for development)

---

## 📆 Project Structure

```
odoo-dev/
├── odoo/               # Odoo Community cloned repo
├── custom_addons/      # Your custom modules
├── config/
│   └── odoo.conf       # Odoo configuration
└── docker-compose.yml  # Service orchestrator
```

---

## 🧰 First Use

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-odoo-project.git
   cd your-odoo-project
   ```

2. Start the services:

   ```bash
   docker compose up -d
   ```

3. Access via browser: [http://localhost:8069](http://localhost:8069)

4. Create a new database:

   - Master password: `admin` (or the one set in `odoo.conf`)

---

## 🐐 Database

The database is a PostgreSQL container fully isolated from your local system. You do **not** need to install PostgreSQL separately.

---

## 🛠 Development

- Place your custom modules inside the `custom_addons/` folder
- The `odoo.conf` is already configured to load modules from there
- Restart the server to apply changes:

  ```bash
  docker compose restart web
  ```

---

## 🧼 Shut everything down

```bash
docker compose down
```

This stops the containers without deleting your data.

---

## 🔁 Restore a database

You can use the "restore a database" option on the Odoo welcome screen to upload a `.zip` exported from Odoo.sh or any other environment.

---
