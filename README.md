# FastAPI Practice Backend 🧪

This project is a personal educational backend built with **FastAPI**, **SQLAlchemy (async)**, **Alembic**, and **PostgreSQL**.  
It is being developed to improve backend development skills, database handling, and API structuring.

Although there is no specific business goal yet, the project simulates a real-world backend architecture and serves as a base for more advanced features in the future.

---

## 🔧 Tech Stack (Current)

- **FastAPI** — lightweight Python web framework for APIs
- **SQLAlchemy (Async ORM)** — database layer
- **PostgreSQL** — relational database
- **Alembic** — migrations management
- **Pydantic** — data validation
- **Uvicorn** — ASGI server

---

## 🚀 Planned Tech Stack (Future)

- **JWT Authentication**
- **OAuth2 / Google login**
- **Docker & Docker Compose**
- **Pytest** for API and DB testing
- **Redis** (caching/session store)
- **Rate limiting**
- **CI/CD (GitHub Actions)**

---

## 🎯 Purpose

This project is built mainly for **learning and portfolio** purposes.  
It's a place to experiment, practice clean architecture, and build up backend intuition with async Python technologies.

---

## 📁 Project Structure (simplified)

```
.
├── api_v1/                 # API routers
│   └── products/           # Product logic (CRUD, schemas, views)
├── core/
│   └── models/             # SQLAlchemy models
├── alembic/                # Alembic migrations
├── .env                    # Environment variables
├── main.py                 # App entrypoint
├── requirements.txt        # Dependencies
└── alembic.ini             # Alembic config
```

---

## 🛠️ How to Run Locally

> ✅ Make sure you have Python 3.10+ and PostgreSQL installed.

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/fastapi-practice-backend.git
cd fastapi-practice-backend
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create `.env` file**

Make a `.env` file in the root directory with your database settings:

```
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_NAME=fastapi_db
```

5. **Run migrations**
```bash
alembic upgrade head
```

6. **Start the server**
```bash
uvicorn main:app --reload
```

Then visit: [http://localhost:8000/docs](http://localhost:8000/docs) to access Swagger UI 🚀

---

## 🧠 Author

Created by **Maxym Horelchyk** — a beginner backend developer learning by building.  
This is a learning sandbox, but parts of it may grow into production-ready components.

---

## 📌 License

MIT License – free to use and modify.