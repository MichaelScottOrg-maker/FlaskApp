# My Flask App

This is a simple Flask web application that includes a login form with fields for a username and password.

## Project Structure

```
my-flask-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── templates
│       └── index.html
├── run.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-flask-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, execute the following command:
```
python run.py
```

The application will be available at `http://127.0.0.1:5000/`. You can access the index page to see the login form.