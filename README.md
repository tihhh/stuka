# Flask Web Application

Web application made with Flask and Bootstrap, using SQLite for database.

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