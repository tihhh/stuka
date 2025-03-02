# Flask Web Application

A web application built with Flask, featuring user authentication and database integration.

## Setup

1. Clone the repository
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies
```bash
pip install flask flask-sqlalchemy python-dotenv
```

4. Set up environment variables
- Copy `.env.example` to `.env`
- Update the `FLASK_SECRET_KEY` in `.env` with your own secret key

5. Run the application
```bash
python main.py
```

## Features
- User authentication (login/signup)
- SQLite database integration
- Bootstrap UI
- Flash messages for user feedback

## Project Structure
```
├── website/
│   ├── __init__.py      # Flask application factory
│   ├── auth.py          # Authentication routes
│   ├── models.py        # Database models
│   ├── views.py         # Main application routes
│   ├── static/          # Static files (CSS, JS)
│   └── templates/       # HTML templates
├── .env                 # Environment variables (not in git)
├── .env.example         # Example environment variables
├── main.py             # Application entry point
└── README.md           # This file
``` 