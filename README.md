✅ FastApiCrudStructural

# FastAPI CRUD Project – Layered Architecture

This repository demonstrates a clean and modular CRUD API built with FastAPI. The project is structured using layered architecture principles including routers, services, and data access layers for better maintainability and scalability.

## Project Overview

- Implements basic CRUD operations (Create, Read, Update, Delete)
- Separates logic into routers, service layer, and data access layer
- Uses Pydantic for data validation
- Can be easily extended to connect with databases (e.g., PostgreSQL)

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn (ASGI server)

## How to Run

1. Clone the repository:
git clone https://github.com/Ghostdevc/FastApiCrudStructural.git
cd FastApiCrudStructural

2. Install dependencies:
pip install -r requirements.txt

3. Run the API server:
uvicorn main:app --reload

4. Open the interactive docs:
- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

## Project Structure

.
├── main.py # FastAPI app entry point
├── routers/ # API endpoints (e.g., users, items)
├── services/ # Business logic
├── models/ # Pydantic schemas
└── repositories/ # Data access layer (can be connected to DB)

## Features

- Modular design using separate layers
- Easy to scale for larger applications
- Fast development using FastAPI + auto-generated documentation

## License

MIT License
