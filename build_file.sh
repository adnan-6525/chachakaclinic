#!/bin/bash
echo "Build started!"

# Install Python dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create a temporary file to indicate successful build
touch .vercel-build-success

# Print a message to indicate the build is complete
echo "Build completed successfully!"
