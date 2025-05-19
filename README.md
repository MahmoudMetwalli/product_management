# Product Management System - Setup Guide

## Prerequisites
- Python 3.x
- PostgreSQL
- Virtual environment

## Installation Steps

### 1. Environment Configuration
```bash
# Copy the environment template file
cp .env.example .env
```
*Edit the `.env` file with your specific configuration values*

### 2. Database Setup
```bash
# Run the database setup script
./db_set_up.sh
```

### 3. Django Setup
```bash
# Run the Django setup script
./django_set_up.sh
```

### 4. Running the Application
```bash
# Start the application from the root directory
uvicorn code_quest_django.asgi:application
```

## Project Structure
```
.
├── Code Quest API.pdf
├── README.md
├── api.md
├── api.yaml
├── code_quest_django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── db_set_up.sh
├── debug.log
├── django_set_up.sh
├── manage.py
├── products
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models
│   │   ├── base_models.py
│   │   ├── brand.py
│   │   ├── keyword.py
│   │   └── product.py
│   ├── repositories
│   │   ├── __pycache__
│   │   ├── brand.py
│   │   ├── keyword.py
│   │   └── product.py
│   ├── serializers
│   │   ├── __pycache__
│   │   ├── brand.py
│   │   ├── keyword.py
│   │   └── product.py
│   ├── services
│   │   ├── __pycache__
│   │   ├── brand.py
│   │   ├── keyword.py
│   │   └── product.py
│   ├── urls.py
│   ├── utils
│   │   ├── __pycache__
│   │   └── is_arabic.py
│   └── views
│       └── api
├── requirements.txt
```

## Development Notes
- Remember to activate your virtual environment before running commands
- All setup scripts should be run from the project root directory
- Check script permissions if you encounter "Permission denied" errors
- Run the server using uvicorn code_quest_django.asgi:application

## Video Links
- Part One: https://youtu.be/TF_vPaFXRnA
- Part Two: https://www.youtube.com/watch?v=Efqa577y-hQ
