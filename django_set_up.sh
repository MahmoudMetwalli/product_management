#!/bin/bash

# Django setup script

# Install Python virtual environment package
echo "Installing python3-venv..."
sudo apt-get update
sudo apt-get install -y python3-venv

# Create and activate virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install uv and dependencies
echo "Installing uv and requirements..."
pip install uv
uv pip install -r requirements.txt

# Run Django migrations
echo "Running Django migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Django setup complete!"
