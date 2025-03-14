# Use the official Python base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies and Python dependencies early for caching
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential && \
  rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app/

# Set permissions and create non-root user
RUN useradd -m app && chown -R app /app
USER app

# Expose port 8000
EXPOSE 8000

# Command to run the Django server 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]