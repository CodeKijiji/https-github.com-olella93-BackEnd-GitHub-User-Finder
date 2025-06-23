# Back-End GitHub User Finder

This project is a Flask application that allows users to find GitHub users and view their profiles and repositories.

## Project Structure

```
phase-4
back-end-github-user-finder/
│
├── server/
│   ├── __init__.py              # Initializes the Flask app
│   ├── app.py                   # Entry point (FLASK_APP=server/app.py)
│   ├── config.py                # Environment config (dev, prod)
│   ├── extensions.py            # Initialize db, JWT, Migrate, etc.
│
│   ├── models/                  # All SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── user.py              # User model (JWT-based auth)
│   │   ├── item.py              # If implementing item catalog
│   │   ├── task.py              # If implementing tasks
│   │   ├── comment.py           # If implementing comments
│
│   ├── controllers/             # Route logic separated by feature
│   │   ├── __init__.py
│   │   ├── auth_controller.py   # Register/login, JWT creation
│   │   ├── user_controller.py   # Profile get/update (protected)
│   │   ├── task_controller.py   # CRUD for tasks (if used)
│   │   ├── item_controller.py   # CRUD for items (if used)
│   │   ├── comment_controller.py# Comment routes
│   │   ├── search_controller.py # GET /api/search
│
│   ├── schemas/                 # Marshmallow schemas for validation (optional)
│   │   ├── __init__.py
│   │   ├── user_schema.py
│   │   ├── item_schema.py
│
│   ├── seed.py                  # Seed the database
│   ├── utils.py                 # Helper functions (token decoding, etc.)
│
├── migrations/                  # Alembic migrations folder
│
├── .env                         # Environment variables
├── .flaskenv                    # FLASK_APP and FLASK_ENV
├── requirements.txt             # All dependencies
├── README.md                    # Setup, auth flow, routes, usage
└── manage.py                    # Optional CLI entrypoint (like Django's manage.py)

```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd Back-End-GitHub-User-Finder
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python app.py
```

The application will be accessible at `http://127.0.0.1:5000`.

## Testing

To run the tests, ensure that the virtual environment is activated and execute:
```
python -m unittest discover -s tests
```

## Contributing

Feel free to submit issues or pull requests for any improvements or bug fixes.