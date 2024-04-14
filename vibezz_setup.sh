#!/bin/bash

# Vibezz Automation Script

# Set Python and Node.js versions
PYTHON_VERSION="3.10"
NODE_VERSION="16.0.0"

# Check if Python and Node.js are installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 could not be found. Please install Python $PYTHON_VERSION or higher."
    exit 1
fi

if ! command -v node &> /dev/null
then
    echo "Node.js could not be found. Please install Node.js $NODE_VERSION or higher."
    exit 1
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Run Flask server
echo "Starting Flask server..."
flask run &

# Start Celery worker
echo "Starting Celery worker..."
celery -A app.celery worker -l info &

# Start Celery beat
echo "Starting Celery beat..."
celery -A app.celery beat -max-interval 2 -l info &

# Navigate to frontend folder
echo "Setting up frontend..."
cd frontend

# Install Node.js dependencies
npm install

# Run Vue.js development server
npm run serve &

echo "Vibezz is now running. Access it at http://localhost:8080"

# Wait for user to stop the script
read -p "Press Enter to stop the Vibezz application..."

# Kill all background processes
echo "Stopping Vibezz application..."
kill $(jobs -p)