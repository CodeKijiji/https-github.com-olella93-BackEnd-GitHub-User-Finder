# GitHub User Finder – Back-End API (Flask + PostgreSQL)

A secure, full-featured REST API built with Flask and PostgreSQL, serving as the backend for the GitHub User Finder application. Includes JWT authentication, profile management, item tracking, comments, search, and refresh token flow.

---

## 🔧 Tech Stack

- Python + Flask
- PostgreSQL
- Flask-JWT-Extended
- SQLAlchemy
- Flask-Migrate
- Flask-Limiter (rate limiting)
- Flask-CORS
- dotenv (.env config)

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/github-user-finder-backend.git
cd github-user-finder-backend

## 2. Create and Activate Virtual Environment

python3 -m venv .venv
source .venv/bin/activate

## 3. Install Dependencies

pip install -r requirements.txt

## 4. Create .env File

DATABASE_URL=postgresql://username:password@localhost:5432/github_user_finder_db
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret-key

Make sure PostgreSQL is running and the github_user_finder_db database exists.

## 5. Run Migrations

export FLASK_APP=server/app.py
export PYTHONPATH=.
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

## Running the Server

flask run

Server runs on: http://127.0.0.1:5000

## Authentication Flow

1. POST /api/register – Register new user (returns JWT access token)

2. POST /api/login – Log in (returns access + refresh token)

3. POST /api/refresh – Refresh expired access token (send refresh token in Authorization header)

## JWT Usage:

For all protected routes, include the access token in the header:

Authorization: Bearer <access_token>
