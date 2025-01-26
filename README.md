# Snippet Organizer

Small project built with Django, which allows for managing code snippets in different languages.

## Features

- User authentication
- Creating, Updating, Deleting and Viewing code snippets
- Syntax highlighting
- Multiple programming languages support

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Virtualenv (optional but recommended)

## Installation

Follow these steps to set up the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/django-project.git
cd django-project
``` 

### 2. Set up a virtual environment (recommended)

Create and activate a virtual environment:

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
``` 

### 3. Install dependencies

Install the required Python packages:
```bash
pip install -r requirements.txt
``` 

### 4. Configure the database

Run migrations to set up the database schema:
```bash
python manage.py migrate
``` 

### 5. Create a superuser (optional)

To create an admin user:
```bash
python manage.py createsuperuser
``` 

Follow the prompts to create the superuser account.

### 6. Run the development server

Start the Django development server:
```bash
python manage.py runserver
``` 

You can now access the application in your browser at:
```bash
http://127.0.0.1:8000
``` 

## Contributing

We welcome contributions! If you'd like to improve this project, please fork the repository, create a new branch, and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
