# Back-End GitHub User Finder

This project is a Flask application that allows users to find GitHub users and view their profiles and repositories.

## Project Structure

```
phase-4
└── Back-End-GitHub-User-Finder
    ├── app.py
    ├── requirements.txt
    ├── README.md
    ├── instance
    │   └── config.py
    ├── static
    ├── templates
    └── tests
        └── test_app.py
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