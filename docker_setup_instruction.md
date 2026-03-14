# Project Setup Guide (Django + Docker)

This document explains how to run the project locally using Docker.

---

## 1. Prerequisites

Install the following tools before running the project:

* Docker
* Docker Compose (Docker Compose v2 is included with Docker Desktop or recent Docker installations)

Verify installation:

```bash
docker --version

docker compose version
```

---

## 2. Clone the Repository

```bash
git clone https://github.com/divyansh251/service_control_panel.git
cd service_hub
```

---

## 3. Project Structure

Expected structure:

```
project-root
│
├── docker-compose.yml
├── .env (optional)
│
└── app
    ├── Dockerfile
    ├── requirements.txt
    ├── manage.py
    └── config
        ├── settings.py
        └── urls.py
```

---

## 4. Build Docker Containers

Run the following command from the project root:

```bash
docker compose build
```

This builds the Docker images for the project.

---

## 5. Start the Project

```bash
docker compose up
```

Run in background:

```bash
docker compose up -d
```

The application will be available at:

```
http://localhost:8000
```

---

## 6. Run Database Migrations

```bash
docker compose exec web python manage.py migrate
```

---

## 7. Create Admin User

```bash
docker compose exec web python manage.py createsuperuser
```

Follow the prompts to create the admin account.

Admin panel:

```
http://localhost:8000/admin
```

---

## 8. Useful Docker Commands

### View running containers

```bash
docker ps
```

### View logs

```bash
docker compose logs -f
```

### Enter the Django container

```bash
docker compose exec web bash
```

### Stop containers

```bash
docker compose down
```

### Rebuild containers

```bash
docker compose up --build
```

---

## 9. Running Django Commands

Examples:

Run migrations:

```bash
docker compose exec web python manage.py migrate
```

Create migrations:

```bash
docker compose exec web python manage.py makemigrations
```

Create superuser:

```bash
docker compose exec web python manage.py createsuperuser
```

---

## 10. Troubleshooting

### Container not starting

Check logs:

```bash
docker compose logs
```

### Rebuild everything

```bash
docker compose down

docker compose up --build
```

### Remove unused containers/networks

```bash
docker system prune
```

---

## 11. Development Workflow

Typical workflow:

```bash
docker compose up -d

docker compose exec web python manage.py migrate

docker compose logs -f
```

Stop when finished:

```bash
docker compose down
```

---

## Notes

* Do not commit `.env` files containing secrets.
* Ensure Docker is running before starting the project.
* Use `docker compose exec web` to run Django management commands.
