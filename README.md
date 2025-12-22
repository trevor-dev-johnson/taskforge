# TaskForge

**TaskForge** is a service-oriented backend API for managing projects and tasks within an organization.

It is built to demonstrate **clean backend architecture**, **explicit domain modeling**, and **reliable data handling** using **Python** and **FastAPI**.

> This project intentionally focuses on backend fundamentals rather than UI or authentication complexity.

---

## ✨ Features

- Project management
- Task creation and assignment
- Enum-backed task status (`todo`, `in_progress`, `done`)
- Controlled task status updates
- Relational data integrity via PostgreSQL
- Clean OpenAPI / Swagger documentation
- Service-layer architecture

---

## 🛠 Tech Stack

- **Python 3.12**
- **FastAPI** — API framework
- **PostgreSQL** — relational database
- **SQLAlchemy 2.0** — ORM
- **Alembic** — database migrations
- **Pydantic v2** — request/response validation

---

## Why TaskForge Exists

TaskForge was built to demonstrate how I design backend systems in a real-world,
correctness-focused way — emphasizing:

- explicit domain boundaries
- database-enforced invariants
- service-layer ownership of business rules
- migration-driven schema evolution

It intentionally avoids UI and auth layers to keep focus on backend structure,
data integrity, and long-term maintainability.

---

## 🧱 Architecture Overview

TaskForge follows a **layered, service-oriented design** that enforces separation of concerns and correctness.

    app/
    ├── api/            # HTTP routes (FastAPI)
    │   └── v1/
    ├── services/       # Business logic
    ├── models/         # SQLAlchemy ORM models
    ├── schemas/        # Pydantic schemas
    ├── db/             # Database session and base
    └── main.py         # Application entrypoint

---

## 📐 Design Principles

- **Thin routes**  
  API routes handle HTTP concerns only

- **Service layer**  
  All business logic lives in services

- **Explicit domain modeling**  
  Enums, foreign keys, and constraints are enforced at the database level

- **Migrations first**  
  Schema changes are handled via Alembic, not runtime magic

---

## 🔄 Task Status Design

Tasks use a **PostgreSQL-backed enum** for status:

    todo
    in_progress
    done

This ensures:

- Only valid states are stored
- API and database remain consistent
- Invalid transitions fail early

Status updates are handled via a dedicated endpoint:

    PATCH /api/v1/tasks/{task_id}/status

---

## 📡 Example API Usage

### Update Task Status

**Request**

    PATCH /api/v1/tasks/42/status
    Content-Type: application/json

    {
      "status": "in_progress"
    }

**Response**

    {
      "id": 42,
      "title": "Write README",
      "description": "Improve project documentation",
      "status": "in_progress",
      "project_id": 3
    }

---

## 🚀 Running Locally

### Prerequisites

- Python 3.12+
- PostgreSQL
- Virtual environment recommended

---

### Setup

    git clone https://github.com/your-username/taskforge.git
    cd taskforge

    python -m venv venv
    source venv/bin/activate     # Windows: venv\Scripts\activate
    pip install -r requirements.txt

---

## 🗄 Database Setup

Create a PostgreSQL database named `taskforge`.

Configure your database connection via environment variables:

    export DATABASE_URL=postgresql://user:password@localhost:5432/taskforge

**Windows (PowerShell)**

    $env:DATABASE_URL="postgresql://user:password@localhost:5432/taskforge"

Run migrations:

    alembic upgrade head

---

## ▶️ Start the API

    uvicorn app.main:app --reload

Swagger UI will be available at:

    http://127.0.0.1:8000/docs

---

## 🔍 Example Workflow (Swagger)

1. Create a project
2. Create tasks for that project
3. Update task status via `PATCH`
4. List tasks by project

All interactions return **clean JSON** and **validated enum values**.

---

## 📌 Project Scope

- No authentication or authorization layer
- No frontend UI
- Focused purely on backend correctness, structure, and maintainability
