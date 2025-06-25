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
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env File

Add the following to a `.env` file in the root directory:

```
DATABASE_URL=postgresql://username:password@localhost:5432/github_user_finder_db
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret-key
```

Make sure PostgreSQL is running and the `github_user_finder_db` database exists.

### 5. Run Migrations

```bash
export FLASK_APP=server/app.py
export PYTHONPATH=.
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Running the Server

```bash
flask run
```

Server runs on: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔑 Authentication Flow

1. `POST /api/register` – Register new user (returns JWT access token)
2. `POST /api/login` – Log in (returns access + refresh token)
3. `POST /api/refresh` – Refresh expired access token (send refresh token in Authorization header)

**JWT Usage:**  
For all protected routes, include the access token in the header:

```
Authorization: Bearer <access_token>
```

---

## 📦 Features

- 🔐 Secure JWT Authentication
- 👤 User Profile Management
- 🗂️ Save and categorize GitHub usernames
- 💬 Comment on saved usernames
- 🔍 Search by GitHub username or note
- 🧪 All endpoints tested in Postman

---

## 📚 API Endpoints

### Auth

| Method | Endpoint        | Description           |
| ------ | --------------- | --------------------- |
| POST   | `/api/register` | Register a new user   |
| POST   | `/api/login`    | Log in and get tokens |
| POST   | `/api/refresh`  | Refresh access token  |

### User Profile

| Method | Endpoint       | Description              |
| ------ | -------------- | ------------------------ |
| GET    | `/api/profile` | Get current user profile |
| PUT    | `/api/profile` | Update user profile      |

### Items (Saved GitHub Users)

| Method | Endpoint          | Description            |
| ------ | ----------------- | ---------------------- |
| POST   | `/api/items/`     | Save a GitHub username |
| GET    | `/api/items/`     | List all saved items   |
| PUT    | `/api/items/<id>` | Update an item         |
| DELETE | `/api/items/<id>` | Delete an item         |

### Comments

| Method | Endpoint                  | Description                            |
| ------ | ------------------------- | -------------------------------------- |
| POST   | `/api/comments/`          | Add a comment to an item               |
| GET    | `/api/comments/<item_id>` | Get comments for a specific item       |
| DELETE | `/api/comments/<id>`      | Delete a comment (if you’re the owner) |

### Search

| Method | Endpoint      | Description                       |
| ------ | ------------- | --------------------------------- |
| GET    | `/api/search` | Search items by keyword (`q` param) |

**Example:**  
`GET /api/search?q=octocat`

---

## 🧪 Postman Testing

1. Register or log in to get an access token.
2. Use `Bearer <access_token>` in headers.
3. Test all endpoints listed above using Postman.
4. For protected routes (e.g., `/api/items`), token must be valid.

---

## 🌱 Seed Data

You can add test data manually via the endpoints or create a custom `seed.py` script if needed.

---

## 📁 Project Structure

```
server/
├── app.py
├── config.py
├── extensions.py
├── models/
│   ├── user.py
│   ├── item.py
│   ├── comment.py
├── controllers/
│   ├── auth_controller.py
│   ├── user_controller.py
│   ├── item_controller.py
│   ├── comment_controller.py
│   └── search_controller.py
└── migrations/
```

---

## 🌐 GitHub Repos

- **Frontend (React):** [https://github.com/CodeKijiji/https-github.com-olella93-FrontEnd-GitHub-User-Finder](https://github.com/CodeKijiji/https-github.com-olella93-FrontEnd-GitHub-User-Finder)
- **Backend (Flask):** [https://github.com/CodeKijiji/https-github.com-olella93-BackEnd-GitHub-User-Finder](https://github.com/CodeKijiji/https-github.com-olella93-BackEnd-GitHub-User-Finder)

---

## 🧠 Author

Richard Olella  
Phase 4 - Moringa School  
[GitHub Profile](https://github.com/olella93)