# Use Python image
FROM python:3.12-slim

# Install system dependencies (FFmpeg + others)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy requirement file
COPY requirements.txt .

# Install python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy full project
COPY . .

# Expose port
EXPOSE 8000

# Final command to run Django on Render
CMD ["gunicorn", "karaoke_project.wsgi:application", "--bind", "0.0.0.0:8000"]
